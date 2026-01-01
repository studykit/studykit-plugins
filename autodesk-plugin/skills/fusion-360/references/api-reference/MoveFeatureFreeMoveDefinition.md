# MoveFeatureFreeMoveDefinition Object

Derived from: [MoveFeatureDefinition](MoveFeatureDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatureFreeMoveDefinition.h>

## Description

The MoveFeatureFreeMoveDefinition object defines a move feature described by a transformation matrix.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MoveFeatureFreeMoveDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](MoveFeatureFreeMoveDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MoveFeatureFreeMoveDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentMoveFeature](MoveFeatureFreeMoveDefinition_parentMoveFeature.htm) | Returns the parent MoveFeature object |
| [transform](MoveFeatureFreeMoveDefinition_transform.htm) | Gets and sets the transform that's applied to the face or body. The matrix must be an orthogonal matrix; that is the axes are perpendicular to each other and there isn't any scaling or mirroring defined.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |