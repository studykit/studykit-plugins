# RecognizedHoles Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/HoleRecognition/RecognizedHoles.h>

## Description

Object that represents a collection of holes.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](RecognizedHoles_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](RecognizedHoles_item.htm) | Returns the hole at the specified index from this collection of holes. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](RecognizedHoles_count.htm) | Returns the number of holes contained in this hole collection. |
| [isValid](RecognizedHoles_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](RecognizedHoles_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[RecognizedHole.recognizeHoles](RecognizedHole_recognizeHoles.htm), [RecognizedHole.recognizeHolesWithInput](RecognizedHole_recognizeHolesWithInput.htm)

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |