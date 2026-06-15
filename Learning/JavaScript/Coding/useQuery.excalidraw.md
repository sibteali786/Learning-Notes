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

import { DependencyList, useEffect, useState } from 'react';

type AsyncState<T> = | 
{status: 'loading'} |
{status: 'error', error: Error} |
{ status: 'success', data: T }

export default function useQuery<T>(fn: () => Promise<T>, deps: DependencyList = []) {
    const [state, setState] = useState<AsyncState<T>>({status: 'loading'})
    useEffect(() => {
        let ignore = false
        async function fetchResult() {
            try{
                const result = await fn()
                if (!ignore) {
                    setState({status: 'success', data: result})
                }
            }catch(e){
                if (!ignore) {
                    setState({status: 'error', error: e as Error})
                }
            }
        }

        fetchResult()
        return () => {
            ignore = true
        }
    },deps)

    return state   
} ^aLvsDe3O

%%
## Drawing
```compressed-json
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
```
%%