# OrientedBoundingBox3D Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/OrientedBoundingBox3D.h>

## Description

Transient object that represents an oriented 3D bounding box. An oriented 3D bounding box is a rectangular box that can be in any orientation in model space. They are created statically using the create method of the OrientedBoundingBox3D class and are used by some functions to return oriented box information.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](OrientedBoundingBox3D_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [contains](OrientedBoundingBox3D_contains.htm) | Determines if the specified point lies within the oriented bounding box. |
| [copy](OrientedBoundingBox3D_copy.htm) | Create a copy of this oriented bounding box. |
| [create](OrientedBoundingBox3D_create.htm) | Creates a transient oriented bounding box object. |
| [setOrientation](OrientedBoundingBox3D_setOrientation.htm) | Sets the orientation of the oriented bounding box. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [centerPoint](OrientedBoundingBox3D_centerPoint.htm) | Gets and sets the centerPoint point of the oriented box. |
| [height](OrientedBoundingBox3D_height.htm) | Gets and sets the height of the oriented bounding box in centimeters. |
| [heightDirection](OrientedBoundingBox3D_heightDirection.htm) | Gets the direction of the height of the oriented bounding box. A unit vector is always returned. |
| [isValid](OrientedBoundingBox3D_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [length](OrientedBoundingBox3D_length.htm) | Gets and sets the length of the oriented bounding box in centimeters. |
| [lengthDirection](OrientedBoundingBox3D_lengthDirection.htm) | Gets the direction of the length of the oriented bounding box. A unit vector is always returned. |
| [objectType](OrientedBoundingBox3D_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [width](OrientedBoundingBox3D_width.htm) | Gets and sets the width of the oriented bounding box in centimeters. |
| [widthDirection](OrientedBoundingBox3D_widthDirection.htm) | Gets the direction of the width of the oriented bounding box. A unit vector is always returned. |

## Accessed From

[BRepBody.orientedMinimumBoundingBox](BRepBody_orientedMinimumBoundingBox.htm), [Component.orientedMinimumBoundingBox](Component_orientedMinimumBoundingBox.htm), [FlatPatternComponent.orientedMinimumBoundingBox](FlatPatternComponent_orientedMinimumBoundingBox.htm), [MeasureManager.getOrientedBoundingBox](MeasureManager_getOrientedBoundingBox.htm), [MeshBody.orientedMinimumBoundingBox](MeshBody_orientedMinimumBoundingBox.htm), [Occurrence.orientedMinimumBoundingBox](Occurrence_orientedMinimumBoundingBox.htm), [OrientedBoundingBox3D.copy](OrientedBoundingBox3D_copy.htm), [OrientedBoundingBox3D.create](OrientedBoundingBox3D_create.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Measure Sample](MeasureSample_Sample.htm) | Measure related functions |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |