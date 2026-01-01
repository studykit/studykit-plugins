# MoveFeaturePointToPointDefinition Object

Derived from: [MoveFeatureDefinition](MoveFeatureDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeaturePointToPointDefinition.h>

## Description

The MoveFeaturePointToPointDefinition object defines a move feature described by the translation from one point to another.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MoveFeaturePointToPointDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](MoveFeaturePointToPointDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MoveFeaturePointToPointDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [originPoint](MoveFeaturePointToPointDefinition_originPoint.htm) | Gets and sets the first point that defines the start position of the move.   To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [parentMoveFeature](MoveFeaturePointToPointDefinition_parentMoveFeature.htm) | Returns the parent MoveFeature object |
| [targetPoint](MoveFeaturePointToPointDefinition_targetPoint.htm) | Gets and sets the second point that defines the direction and distance of the move.   To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |