# bluroma-py
Attempt at making a Pleroma/Akkoma-like Bluesky client in Python. It's not gonna be good.
> [!CAUTION]
> This is not ready for production yet.

## To-do
A lot.

### Basic
List of things to implement before moving into a public beta
* Login
  * OAuth
  * Support for third-party PDSes (DONE)
  * Remember your session (functional but needs to be rebuilt)
* Client
  * Dashboard
  * Settings
  * All of the below
* Posts
  * Viewing posts
  * Making posts
  * Browsing replies
* Profiles
  * Seeing them
  * Interacting with them
* Interactions
  * Likes
  * Boosts
  * Blocks
  * Mutes
  * All of it
* Database
  * Initialization and migrations (done, migrations might need to be approved)
  * Store user sessions and data
* User settings
  * Basic Bluesky settings

### Future
Cool ideas that I feel would make up a "stable" release
* Interoperability / Federation (is some of this even possible with the atproto library?)
  * List links to ATproto tools
  * Show something for third-party AppViews
  * "Enhanced" Bridgy Fed posts (full post data is stored inside of the records, not used by Bluesky i.e. can be used by third party clients)
  * Account migrations
* Customization
  * Themes
  * Moderation
    * Bypassing blocked posts
    * Respecting the "users demands authentication" check