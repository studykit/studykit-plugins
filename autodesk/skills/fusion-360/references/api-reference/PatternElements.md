# PatternElements Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatternElements.h>

## Description

Collection that provides access to pattern elements of mirror and pattern features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](PatternElements_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](PatternElements_item.htm) | Function that returns the specified pattern element using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](PatternElements_count.htm) | The number of pattern elements in the collection. |
| [isValid](PatternElements_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](PatternElements_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CircularPatternFeature.patternElements](CircularPatternFeature_patternElements.htm), [MirrorFeature.patternElements](MirrorFeature_patternElements.htm), [PathPatternFeature.patternElements](PathPatternFeature_patternElements.htm), [RectangularPatternFeature.patternElements](RectangularPatternFeature_patternElements.htm)

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |