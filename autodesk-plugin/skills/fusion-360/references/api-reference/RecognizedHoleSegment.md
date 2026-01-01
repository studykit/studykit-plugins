# RecognizedHoleSegment Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/HoleRecognition/RecognizedHoleSegment.h>

## Description

Object that represents a hole segment, i.e. a single geometric shape like a cylinder or cone within the context of a hole. A segment represents a hole face.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](RecognizedHoleSegment_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [axis](RecognizedHoleSegment_axis.htm) | Returns the unit vector that points straight up out of the segment in the global coordinate system. |
| [bottomDiameter](RecognizedHoleSegment_bottomDiameter.htm) | Returns the diameter of the bottom of this segment. |
| [face](RecognizedHoleSegment_face.htm) | \*\*RETIRED\*\* Returns the model face this segment references. |
| [faces](RecognizedHoleSegment_faces.htm) | Returns the model faces this segment references. |
| [halfAngle](RecognizedHoleSegment_halfAngle.htm) | For hole segments of type Cone, returns the cone's half angle, i.e. the angle between the axis of the cone and its surface. Returns 0 for other segment types. |
| [height](RecognizedHoleSegment_height.htm) | Returns the height of this segment from top to bottom. |
| [holeSegmentType](RecognizedHoleSegment_holeSegmentType.htm) | Returns whether this segment represents a cylinder, cone, flat, or torus geometry type |
| [isThreaded](RecognizedHoleSegment_isThreaded.htm) | Returns true if this segment is threaded, i.e. associated with a thread feature. |
| [isValid](RecognizedHoleSegment_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](RecognizedHoleSegment_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [threadFeatures](RecognizedHoleSegment_threadFeatures.htm) | Returns the thread features associated with this segment, or null if none exist for this segment. |
| [topDiameter](RecognizedHoleSegment_topDiameter.htm) | Returns the diameter of the top of this segment. |

## Accessed From

[RecognizedHole.segment](RecognizedHole_segment.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Hole and Pocket Recognition API Sample](HoleAndPocketRecognition_Sample.htm) | This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.  The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.  RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.  The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.  This script works only if the Manufacturing Extension is active. |

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |