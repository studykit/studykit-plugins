# UntrimFeatureInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UntrimFeatureInput.h>

## Description

This class defines the methods and properties that pertain to the definition of an Untrim feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](UntrimFeatureInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [setLoops](UntrimFeatureInput_setLoops.htm) | Set the loops to be removed. |
| [setLoopsFromFaces](UntrimFeatureInput_setLoopsFromFaces.htm) | Set the loops to be removed from a set of faces. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [extensionDistance](UntrimFeatureInput_extensionDistance.htm) | Gets and sets the ValueInput object that defines the extension distance applied to faces when an external boundary is removed. |
| [facesToUntrim](UntrimFeatureInput_facesToUntrim.htm) | Gets the face objects to untrim. Returns null/None in the case where loops are specified instead of faces. |
| [isValid](UntrimFeatureInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [loopsToUntrim](UntrimFeatureInput_loopsToUntrim.htm) | Gets the loop objects to untrim. Returns null/None in the case where faces are specified instead of loops |
| [objectType](UntrimFeatureInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [untrimLoopType](UntrimFeatureInput_untrimLoopType.htm) | Gets the loop type to be untrimmed. This is only used when faces are being untrimmed and is ignored for loops. |

## Accessed From

[UntrimFeatures.createInputFromFaces](UntrimFeatures_createInputFromFaces.htm), [UntrimFeatures.createInputFromLoops](UntrimFeatures_createInputFromLoops.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Untrim Feature API Sample](UntrimFeatureSample_Sample.htm) | Demonstrates creating a new untrim feature. |

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |