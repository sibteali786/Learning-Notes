---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
useQuery ^ZDwjh4p2

What we need ^dquXap3u

- should run async fucntions and return their response
- should return status with values like loading, error and success
- should return data if resolved successfully
- should handle deps change ^QSpW14H1

export default useQuery(fn, deps = []){
    const [status, setStatus] = useState<'loading' | 'error' | 'success'>()
    const [error, setError] = useState<Error>(null)
    const [data, setData] = useState(null)
    
    useEffect(() => {
        async function fetchResult  {
            try{
                setStatus('loading');
                const result = await fn();
                if ( !ignore){
                    setStatus('success');
                    setData(result)
                }
            }catch(error) {
                if ( !ignore ) {
                    setStatus('error')
                    setError(error)
                }
                
            }
        }

        let ignore = false
        fetchResult()
        return () => {
          ignore = true;
        }
    },deps)
    if (status === 'loading') {
        return {status}    
    }
    if (status === 'error') {
        return {status, error}    
    }
    return {
        status,
        data
    }
 } ^z0hZqwaQ

import { DependencyList, useEffect, useState } from 'react';

type AsyncState<T> = 
    | {status: 'loading'}
    | {status: 'error' , error: Error}
    | {status: 'success', data: T}
export default useQuery<T>(fn: Promise<T>, deps: DependencyList = []){
    const [state, setState] = useState<AsyncState<T>>({
        status: 'loading',
    })    
    useEffect(() => {
        async function fetchResult  {
            try{
                const result = await fn();
                if ( !ignore){
                    setState({ status: 'success', data });
                }
            }catch(error) {
                if ( !ignore ) {
                    setState({ status: 'error', error });
                }
            }
        }

        let ignore = false
        fetchResult()
        return () => {
          ignore = true;
        }
    },deps)
    if (status === 'loading') {
        return {status}    
    }
    if (status === 'error') {
        return {status, error}    
    }
    return {
        status,
        data
    }
 } ^sYuqkIE6

This version uses Type / Typescript and also take care of three states in a single state unlike last solution which uses three different states ^gjIKWdCP

%%
## Drawing
```compressed-json
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
```
%%