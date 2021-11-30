# project-julialfk

## Problem statement

While all browsers have the option to deny third party cookies and delete all cookies after closing the browser,
the user still has to go through the cookie statement popup every time they open a new page on a new session.
There are browser extensions, like *Ninjacookie* that provide a solution to this problem, but these are not
available for mobile or other non-desktop devices.

## Solution sketch

This application will automatically deny all third party cookies automatically for every device that is connected
to the same network as the server

## Prerequisites

### Similar apps

There are similar existing browser extensions that take care of cookie popups in different ways.
These are the most frequently used ones:

[Consent-O-Matic](https://github.com/cavi-au/Consent-O-Matic) is a browser extension that automatically submits your preset cookie preferences.

[Ninjacookie](https://ninja-cookie.com/) and [Consent Manager](https://github.com/privacycloud/consent-manager-web-ext) do not accept any unnecessary cookies when a popup appears.

[I don't care about cookies](https://www.i-dont-care-about-cookies.eu/) simply gets rid of the whole cookie popup.
However, as a result all cookies might be accepted if third party cookies are not turned off in the browser settings.

The main difference between this containerized app and the existing browser extensions will be that the container app will only work on a single wifi network.
This means that all devices connected to the network will not show any cookie popups and refuse all unnecessary cookies.

### Hardest parts

While it is preferable to automate denying cookies when prompted, it might turn out to be too difficult for me to implement.
If this is the case, I might opt to design a program similar to *I don't care about cookies*, where the popup will simply
be deleted.

Making the program recognize all devices on the same network might prove to be challenging as well.
As such, while it would not make the app functionally different from similar apps, I might have to decide to only make the app work locally.
