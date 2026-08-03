---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
function useLazyImage(src, options = {}) {
    const [imageSrc, setImageSrc] = useState(null)
    const [isLoaded, setIsLoaded] = useState(null)
    const ref = useRef(null)
    
    useEffect(()=>{
        const el = ref.current;
        if (!el) return;
        
        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach(entry => {
                    if (entry.isInteresting){
                        setImageSrc(src);
                        observer.unobserve(el);
                    }
                })
            }, {
                root: options.root, 
                rootMargin: options.rootMargin || '200px',
                threshold: options.threshold || 0.1,
            }
        )
        },[src, options.root, options.rootMargin, options.threshold])
        observer.observe(el);
        return () => observer.disconnect();
    return {ref, imageSrc, isLoaded, setIsLoaded}
} ^ngu9pWYT

function LazyImage({ src, alt }) {
  const { ref, imageSrc, isLoaded, setIsLoaded } = useLazyImage(src);

  return (
    <div ref={ref} style={{ minHeight: 200, background: '#1a1d29' }}>
      {imageSrc && (
        <img
          src={imageSrc}
          alt={alt}
          onLoad={() => setIsLoaded(true)}
          style={{ opacity: isLoaded ? 1 : 0, transition: 'opacity 0.3s' }}
        />
      )}
    </div>
  );
} ^znGOhm2h

%%
## Drawing
```compressed-json
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

mpANyMEM6FBCAJBEAA==
```
%%