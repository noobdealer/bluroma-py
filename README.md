<img src="meta/logo.png" alt="The Bluroma logo, containing three rectangles with one rounded corner each shaped to look like an uppercase B and the Bluroma name written in the Convection font beside it." width="200">

## About
This is an attempt at making a Pleroma/Akkoma-like Bluesky client in Python. It's not gonna be good. Currently being built by [@noob.quest](https://bsky.app/profile/noob.quest).
> [!CAUTION]
> This is not ready for production yet, but this shouldn't be a surprise.

## To-do
A lot.

### Basic
List of things to implement before I can feel like it's worth hosting somewhere.
* Login
  * OAuth
  * Support for third-party PDSes (DONE)
  * Remember your session (functional but needs to be rebuilt because it's busted)
* Client
  * Dashboard (Base template just needs to be made functional)
  * Settings
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
  * Initialization and migrations (done, migrations might need to be improved later on)
  * Store user sessions and data
* User settings
  * Basic Bluesky settings

### Future
Cool ideas that I feel would make up a "stable" release
* Interoperability / Federation (is some of this even possible with the atproto library?)
  * List links to ATproto tools
  * Show something for third-party AppViews
  * "Enhanced" Bridgy Fed posts (full post data is stored inside of the records, not used by Bluesky but can be used by third party clients)
  * Integrated account migrations
* Customization
  * Themes
  * Moderation
    * Bypassing blocked posts
    * Respecting the "users demands authentication" 

## Credits
* Shoutout to the [Pleroma](https://pleroma.social) and [Akkoma](https://akkoma.social) developers for all of their work, which I've shamelessly copied.
* Thank you to [MarshalX](https://bsky.app/profile/marshal.dev) for building the ATproto Python packages that I use.