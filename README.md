# dkPyTalk
The Internet of Swings for Code &amp; Supply on March 22nd

## About this talk
I wanted to do a live coding session to walk everyone through the getting started portions of Django, matplotlib, and numpy, but realized that even in the best scenario I couldn't finish everything in 40 minutes, even with notes in front of me. So I decided to do a hybrid code/talk on top of `git` and `README.md`. To follow along in the talk, the different steps are organized into [branches](https://github.com/mressler/dkPyTalk/branches) that you can checkout and diff between to see the updates.

As of the most recent version of _this_ file there are 6 steps:
1. [Step 0](https://github.com/mressler/dkPyTalk/tree/step-0) - Environment Setup
2. [Step 1](https://github.com/mressler/dkPyTalk/tree/step-1) - Django scaffolding & Hello world!
3. [Step 2](https://github.com/mressler/dkPyTalk/tree/step-2) - Add some model objects
4. [Step 3](https://github.com/mressler/dkPyTalk/tree/step-3) - Apply a SQL migration and add some bootstrap data, explore the QuerySet API
5. [Step 4](https://github.com/mressler/dkPyTalk/tree/step-4) - Turn CSVs into numpy matrices, slice them up and feed them to matplotlib. Delicious.
6. [Step 5](https://github.com/mressler/dkPyTalk/tree/step-5) - Send our beautiful plots back out through Django

Hopefully you'll come away with the ability to get your own data driven Django setup off the ground and avoid some of the pitfalls I ran into along the way.

## Diamond Kinetics
Diamond Kinetics is a baseball motion capture company based in Pittsburgh, PA that uses inertial measurement units (IMUs) to record and analyze baseball and softball swings. The swing motion is very complex, but using these sensitive IMUs, Diamond Kinetics can recreate the entire motion of the swing in three dimensions.

Included here are just a few simplified data sets that will highlight the interaction possible with Django, numpy, and matplotlib.
