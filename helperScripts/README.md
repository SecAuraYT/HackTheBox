# Helper scripts used in SecAura's Hackthebox/similar videos.
Most often just automates taking the Hackthebox vpn ip and printing it in some form, like in a reverse shell string, or curl etc.
e.g
![image](https://user-images.githubusercontent.com/93036504/151440306-49ffdba7-b89c-4d79-bf5f-21c071f229b8.png)


## Web server wrappers
>(prints some download/invoke string wrapped around interface `tun0` IP + sets up `python` webserver to catch requests)

| name        | Description           |
| ------------- |:-------------:|
| web | Shortcut to spawn python webserver|
| lcweb | `curl` wrapped IP, that pipes output to `bash`|
| lweb | `wget`  wrapped IP |
| pweb | `powershell` invoker wrapped IP |
| pweb_dl | `powershell` downoader wrapped IP |
| pweb_enc | `powershell` base64 encoded payload invoker |
### SMB
| name        | Description           |
| ------------- |:-------------:|
| smb_cp | `smb` unc path windows downloader string |
| smb_dl | `smb` unc path windows invoker string (runs path2file via powershell to avoid writing to disk)|

## Other
| name        | Description           |
| ------------- |:-------------:|
| shellz | prints rev shell strings, and sets up a netcat listener wrapper with RLWRAP, for added functionality|
