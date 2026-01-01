# LoftSmoothEndCondition Object

Derived from: [LoftEndCondition](LoftEndCondition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftSmoothEndCondition.h>

## Description

Represents a "Smooth" loft end condition.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](LoftSmoothEndCondition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](LoftSmoothEndCondition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](LoftSmoothEndCondition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentLoftSection](LoftSmoothEndCondition_parentLoftSection.htm) | Returns the parent loft section. |
| [weight](LoftSmoothEndCondition_weight.htm) | Gets the valueInput or Parameter that defines the weight of the loft. If this object was obtained from a LoftFeatureInput object then this will return a valueInput object with the initial value provided. If this object was obtained from an exiting LoftFeature then it returns a Parameter. In the case of a parameter, to change the weight, edit the value of the associated parameter. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |