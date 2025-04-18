const username = "admin";

function renderPost(post) {
    const template = document.getElementById("post-template").content.cloneNode(true);
    template.querySelector(".username").innerText = post.username;
    template.querySelector(".message").innerText = post.message;
    document.getElementById("feed").appendChild(template);
}

function submitPost() {
    const message = document.getElementById("postInput").value;
    console.log("Would post:", message);
    alert("Tweet submitted (not really yet)");
}

window.onload = async () => {   // async -> run parrlel to other code
    try {
        const response = await fetch("/api/posts");
        const posts = await response.json();
        posts.forEach((post) => renderPost(post));  // loop through posts
    } catch (error) {
        console.error("FIX THISSSS:", error);
    }
    renderPost(hardcodedPost);
};
