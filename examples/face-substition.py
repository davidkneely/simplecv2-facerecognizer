#!/usr/bin/env python
#
# Released under the BSD license. See LICENSE file for details.
"""
All this example does is find a face and replace it with another image. The
image should auto scale to match the size of the face.
"""
print __doc__

from simplecv import Camera, Display, HaarCascade, Image

#initialize the camera
cam = Camera()
# Create the display to show the image
display = Display()

# Load the new face image
troll_face = Image('troll_face.png', sample=True)

# Haar Cascade face detection, only faces
haarcascade = HaarCascade("face")

# Loop forever
while display.isNotDone():
    # Get image, flip it so it looks mirrored, scale to speed things up
    img = cam.getImage().flip_horizontal().scale(0.5)
    # load in trained face file
    faces = img.find_haar_features(haarcascade)
    # If there were faces found do something
    if faces:
        face = faces[-1]
        # Load the image to super impose and scale it correctly
        troll = troll_face.scale(face.get_height(), face.get_width())
        mymask = troll.invert()
        # Super impose the new face on the existing face
        img = img.blit(troll, face.top_left_corner(), alpha_mask=mymask)
    # Display the image
    img.save(display)
