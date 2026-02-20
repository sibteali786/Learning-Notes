```table-of-contents
```
## **NestJS Core Concepts**

### **1. Modules (`@Module`)**

Think of modules as **containers** that group related code together.

```typescript
@Module({
  imports: [TypeOrmModule.forFeature([User]), PassportModule, JwtModule],
  providers: [AuthService, JwtStrategy],
  controllers: [AuthController],
  exports: [AuthService],
})
export class AuthModule {}
```

**Breaking it down:**

- `imports`: Other modules this module needs (like importing libraries)
- `providers`: Services/strategies that can be injected (dependency injection)
- `controllers`: Handle HTTP requests (routes)
- `exports`: Make providers available to other modules

**Why?** Modules organize code and manage dependencies. NestJS uses them to build a dependency injection tree.

---

### **2. Dependency Injection (DI)**

**Problem**: How do services get instances of other services they need?

**Traditional way (bad)**:

```typescript
class AuthService {
  constructor() {
    this.userRepo = new UserRepository(); // ❌ Hard to test, tightly coupled
  }
}
```

**NestJS way (good)**:

```typescript
@Injectable()
class AuthService {
  constructor(
    @InjectRepository(User) private userRepo: Repository<User>,
    private jwtService: JwtService,
  ) {}
}
```

**What happens:**

1. `@Injectable()` tells NestJS: "This class can be injected into other classes"
2. NestJS sees the constructor parameters
3. NestJS automatically creates and injects instances
4. You get fresh, properly configured instances without manual setup

**Why?**

- Easy testing (can mock dependencies)
- Loose coupling (swap implementations easily)
- Single instance per app (singleton pattern)

---

### **3. Providers**

Providers are **anything that can be injected**. In our auth module:

```typescript
providers: [AuthService, JwtStrategy]
```

**AuthService** - Business logic for registration/login **JwtStrategy** - Tells Passport.js how to validate JWT tokens

**Registration process:**

```typescript
@Module({
  providers: [AuthService], // 1. Register AuthService
})

@Injectable() // 2. Mark as injectable
export class AuthService {
  constructor(private jwtService: JwtService) {} // 3. Inject dependencies
}
```

---

## **Authentication Flow - How It All Works Together**

### **Registration/Login Flow**

```
User Request → Controller → Service → Database → Response
```

**1. Controller receives request:**

```typescript
@Controller('auth')
export class AuthController {
  constructor(private authService: AuthService) {} // DI injects AuthService

  @Post('register') // Handles POST /auth/register
  register(@Body() dto: RegisterDto) { // @Body() extracts request body
    return this.authService.register(dto);
  }
}
```

**Decorators explained:**

- `@Controller('auth')`: Creates routes under `/auth`
- `@Post('register')`: Handles POST requests to `/auth/register`
- `@Body()`: Extracts and validates JSON body using DTOs

---

**2. Service handles business logic:**

```typescript
@Injectable()
export class AuthService {
  constructor(
    @InjectRepository(User) private userRepo: Repository<User>,
    private jwtService: JwtService,
  ) {}

  async register(dto: RegisterDto) {
    // 1. Check if user exists
    const exists = await this.userRepo.findOne({ where: { email: dto.email } });
    
    // 2. Hash password
    const passwordHash = await bcrypt.hash(dto.password, 10);
    
    // 3. Create user
    const user = this.userRepo.create({ ...dto, passwordHash });
    await this.userRepo.save(user);
    
    // 4. Generate JWT token
    const token = this.jwtService.sign({ sub: user.id, email: user.email });
    
    return { user, token };
  }
}
```

**`@InjectRepository(User)`**: Special decorator from TypeORM that injects a repository for the User entity. Repository = database access layer.

---

### **JWT Authentication Strategy**

**The Problem**: How does NestJS know if a token is valid?

**The Solution**: Passport.js + Strategy Pattern

```typescript
@Injectable()
export class JwtStrategy extends PassportStrategy(Strategy) {
  constructor(
    private config: ConfigService,
    private authService: AuthService,
  ) {
    super({
      jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(), // Where to find token
      secretOrKey: config.get<string>('JWT_SECRET'), // Secret to verify signature
    });
  }

  async validate(payload: JwtPayload) {
    // This runs AFTER token is verified
    const user = await this.authService.validateUser(payload.sub);
    if (!user) {
      throw new UnauthorizedException();
    }
    return user; // Attached to request.user
  }
}
```

**Step-by-step:**

1. User sends: `Authorization: Bearer <token>`
2. `ExtractJwt.fromAuthHeaderAsBearerToken()` extracts token
3. JWT library verifies signature using `JWT_SECRET`
4. If valid, `validate()` method runs
5. `validate()` checks if user still exists in DB
6. User object attached to `request.user`

---

### **Guards - Protecting Routes**

**Without guard (anyone can access):**

```typescript
@Get('profile')
getProfile() {
  return { message: 'Public route' };
}
```

**With guard (only authenticated users):**

```typescript
@UseGuards(JwtAuthGuard)
@Get('profile')
getProfile(@Request() req) {
  return req.user; // User from JwtStrategy.validate()
}
```

**What `@UseGuards(JwtAuthGuard)` does:**

1. Intercepts request before controller
2. Runs JwtStrategy validation
3. If valid → proceed to controller
4. If invalid → return 401 Unauthorized

**JwtAuthGuard:**

```typescript
@Injectable()
export class JwtAuthGuard extends AuthGuard('jwt') {}
```

`AuthGuard('jwt')` → Tells Passport to use JwtStrategy

---

## **How It All Connects - Complete Flow**

### **Scenario: User logs in and accesses protected route**

**Step 1: Login**

```
POST /auth/login
Body: { email, password }
     ↓
AuthController.login()
     ↓
AuthService.login()
     ↓
1. Find user in DB (userRepo.findOne)
2. Verify password (bcrypt.compare)
3. Generate JWT (jwtService.sign)
     ↓
Response: { user, token }
```

**Step 2: Access protected route**

```
GET /projects
Headers: Authorization: Bearer <token>
     ↓
@UseGuards(JwtAuthGuard) intercepts
     ↓
JwtStrategy runs:
  1. Extract token from header
  2. Verify signature
  3. Run validate() method
  4. Load user from DB
  5. Attach user to request
     ↓
ProjectsController.findAll()
  - Can access req.user
     ↓
Response: [...projects]
```

---

## **Key NestJS Patterns Used**

### **1. Decorator Pattern**

```typescript
@Injectable()  // Marks class for DI
@Controller('auth')  // Defines base route
@Post('login')  // Defines HTTP method
@Body()  // Extracts request body
@UseGuards(JwtAuthGuard)  // Adds authentication
```

**Why?** Clean, readable syntax. Metadata for NestJS to wire things together.

---

### **2. Dependency Injection**

```typescript
constructor(
  private authService: AuthService,  // NestJS injects this
  private config: ConfigService,      // And this
) {}
```

**Why?** No manual instantiation. Easy testing. Single responsibility.

---

### **3. Strategy Pattern (Passport.js)**

```typescript
export class JwtStrategy extends PassportStrategy(Strategy) {
  async validate(payload: JwtPayload) {
    // Custom validation logic
  }
}
```

**Why?** Swappable authentication strategies. Could add GoogleStrategy, FacebookStrategy, etc.

---

### **4. Data Transfer Objects (DTOs)**

```typescript
export class LoginDto {
  @IsEmail()
  email: string;

  @IsString()
  password: string;
}
```

**Why?**

- Validation (class-validator checks @IsEmail automatically)
- Type safety
- Self-documenting API

---

## **Visual Summary**

```
┌─────────────────────────────────────────────────────────────┐
│                        AuthModule                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ AuthController│  │ AuthService  │  │ JwtStrategy  │      │
│  │              │  │              │  │              │      │
│  │ @Post login  │→ │ validate pwd │  │ validate JWT │      │
│  │ @Post register│→ │ create user  │  │ load user    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│         ↓                  ↓                  ↓              │
│    HTTP Request       Business Logic    Token Validation    │
└─────────────────────────────────────────────────────────────┘
         ↓                  ↓                  ↓
    ┌─────────┐      ┌──────────┐      ┌──────────┐
    │ DTOs    │      │ TypeORM  │      │ Passport │
    │Validation│      │ Database │      │   JWT    │
    └─────────┘      └──────────┘      └──────────┘
```

---

## **Common Questions**

**Q: Why not just use Express middleware?** A: NestJS DI + decorators give better structure, testing, and type safety.

**Q: What's the difference between Service and Controller?** A: Controller = routes (HTTP), Service = business logic (reusable).

**Q: Why use strategies?** A: Easily swap auth methods (JWT → OAuth → API Keys) without changing controllers.

**Q: When do I use @Injectable()?** A: Any class that needs to be injected OR needs to inject other dependencies.

---

**Does this clarify how everything connects? Want me to explain any specific part deeper?**