# Postmortem: The Day Our E-Commerce Platform Slowed to a Crawl

## Issue Summary

- **Duration:** 2 hours and 15 minutes, from 12:30 PM GMT+1 to 2:45 PM GMT+1 
- **Impact:** Our e-commerce platform, usually busy with shoppers, suddenly became very slow, and it was like a deserted town for our loyal customers. This affected everyone, and no one could look at products, buy anything, or access their account.
- **Root Cause:** Our load balancer, which manages our web traffic, got overwhelmed by a sudden rush of visitors. It decided to stop working, causing it to refuse to send visitors to our main servers.

## Timeline

- **12:20 PM PST:** Our monitoring systems, which usually quietly keep an eye on our platform, started making loud alerts. They noticed that our e-commerce website was becoming slow.
- **12:25 PM PST:** Our alert engineers quickly went to check what was happening. They found that our load balancer was sending way too much traffic to one of our servers.
- **12:30 PM PST:** The overloaded server couldn't handle all the traffic and crashed, causing the entire e-commerce website to go offline.
- **12:35 PM PST:** We got our emergency response team involved to fix the issue.
- **12:40 PM PST:** Our emergency response engineers, with their technical knowledge and some strong coffee, found that the problem was a mistake in the load balancer's settings.
- **1:15 PM PST:** After making careful adjustments and keeping a close watch, our engineers managed to convince the load balancer to start working correctly again.
- **2:00 PM PST:** The overloaded server had recovered and was slowly getting back to work. Our e-commerce website began to work again.
- **2:45 PM PST:** The e-commerce website was fully back to normal, and customers could shop, make purchases, and access their accounts again.

## Root Cause and Resolution

- **Root Cause:** The problem was a mistake in how our load balancer was set up, like a traffic signal showing the wrong direction, causing a big traffic jam that stopped everything.
- **Resolution:** Our engineers fixed the load balancer's settings to make sure it wouldn't cause traffic problems in the future.

## Corrective and Preventive Measures

- **Better setup management:** We're going to be more careful with our settings, treating them like valuable recipes that need thorough testing.
- **Enhanced monitoring:** We're improving our monitoring systems to act like a network of security cameras, always watching for any problems.
- **Automatic alerts:** We're setting up automatic alerts, like fire alarms, to tell us when there might be issues.
- **Stress testing:** We're going to give our e-commerce website a workout, simulating high traffic to find and fix problems before they cause trouble.
- **Backup systems:** Like a chef preparing extra dishes in case something goes wrong, we're adding backup load balancers and servers to keep things running smoothly.

## Lessons Learned

This incident taught us that even well-prepared systems can have problems. We're committed to making our e-commerce platform more reliable and ready to serve our customers, no matter what.

