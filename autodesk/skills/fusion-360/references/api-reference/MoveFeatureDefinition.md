# MoveFeatureDefinition Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatureDefinition.h>

## Description

A Base class to return the information used to define a Move feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MoveFeatureDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](MoveFeatureDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MoveFeatureDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentMoveFeature](MoveFeatureDefinition_parentMoveFeature.htm) | Returns the parent MoveFeature object |

## Accessed From

[MoveFeature.definition](MoveFeature_definition.htm)

## Derived Classes

[MoveFeatureFreeMoveDefinition](MoveFeatureFreeMoveDefinition.htm), [MoveFeaturePointToPointDefinition](MoveFeaturePointToPointDefinition.htm), [MoveFeaturePointToPositionDefinition](MoveFeaturePointToPositionDefinition.htm), [MoveFeatureRotateDefinition](MoveFeatureRotateDefinition.htm), [MoveFeatureTranslateAlongEntityDefinition](MoveFeatureTranslateAlongEntityDefinition.htm), [MoveFeatureTranslateXYZDefinition](MoveFeatureTranslateXYZDefinition.htm)

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |