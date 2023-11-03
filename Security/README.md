<h1>Token vs Session based Authentication</h1>
<h3>
In the context of modern APIs, token-based authentication is more common and widely preferred over traditional session-based authentication. Token-based authentication has become the de facto standard for securing APIs for below reasons:  
</h3>
<h3>Statelessness:</h3>
<p>
APIs are designed to be stateless, meaning they do not store session information on the server. Token-based authentication aligns well with this architectural principle, as each request can be authenticated independently, without the need to maintain session state on the server.
</p>

<h3>
Scalability:  
</h3>
<p>
 Token-based authentication is highly scalable. Since there is no server-side session state to manage, it's easier to scale API servers horizontally to handle increased traffic and demand. 
</p>

 <h3>
Cross-Origin Requests:   
 </h3>
 <p>
 APIs are often accessed by various clients, including web browsers, mobile apps, and third-party applications. Token-based authentication is compatible with cross-origin requests, making it suitable for a diverse range of clients.  
 </p>
 
