// Let&apos;s type this into the console, follow along with the video lecture

var x = document.querySelector(&quot;p&quot;)

// Show Text
x.textContent

// Reassign Text
x.textContent = &quot;new&quot;

// Refresh the page
// Show actual HTML
x.innerHTML

// Edit HTML
x.innerHTML = &quot;This is &lt;strong&gt;BOLD&lt;/strong&gt;&quot;

// Can&apos;t do that with just textContent

/////////////////
// Attributes //
///////////////

var special = document.querySelector(&quot;#special&quot;)
var specialA = y.querySelector(&quot;a&quot;)

specialA.getAttribute(&quot;href&quot;)

specialA.setAttribute(&quot;href&quot;,&quot;https://www.amazon.com&quot;)
