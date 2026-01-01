# PatternElement Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatternElement.h>

## Description

This class defines the properties that pertain to the pattern element.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](PatternElement_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [faces](PatternElement_faces.htm) | Gets the faces generated as a result of this particular element. |
| [id](PatternElement_id.htm) | Gets the id of this element within the pattern. |
| [isSuppressed](PatternElement_isSuppressed.htm) | Gets and sets whether the element is suppressed or not. A value of True indicates it is suppressed |
| [isValid](PatternElement_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](PatternElement_name.htm) | Get the name of the pattern element. |
| [objectType](PatternElement_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [occurrences](PatternElement_occurrences.htm) | If the patternEntityType property of the parent feature returns OccurrencesPatternType then this property will return the occurrences associated with this particular pattern element. |
| [parentFeature](PatternElement_parentFeature.htm) | Gets the feature pattern this element is a member of. |
| [transform](PatternElement_transform.htm) | Get the transform that describes this elements relative position to the parent object(s). The transform returned for the first element in a pattern will be an identity matrix. |

## Accessed From

[PatternElements.item](PatternElements_item.htm)

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |