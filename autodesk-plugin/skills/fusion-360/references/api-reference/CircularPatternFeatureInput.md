# CircularPatternFeatureInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CircularPatternFeatureInput.h>

## Description

This class defines the methods and properties that pertain to the definition of a circular pattern feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CircularPatternFeatureInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [axis](CircularPatternFeatureInput_axis.htm) | Gets and sets the axis of circular pattern. This can be a sketch line, linear edge, construction axis, an edge/sketch curve that defines an axis (circle, etc.) or a face that defines an axis (cylinder, cone, torus, etc.). |
| [inputEntities](CircularPatternFeatureInput_inputEntities.htm) | Gets and sets the input entities. The collection can contain faces, features, bodies or occurrences. All of the entities must be of a single type. For example, it can't contain features and occurrences but only features or occurrences. |
| [isSymmetric](CircularPatternFeatureInput_isSymmetric.htm) | Gets and sets if the angle extent is in one direction or symmetric. |
| [isValid](CircularPatternFeatureInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CircularPatternFeatureInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [patternComputeOption](CircularPatternFeatureInput_patternComputeOption.htm) | Gets and sets the compute option when patterning features. The default value for this is AdjustPatternCompute. This property only applies when patterning features and is ignored in the direct modeling environment. |
| [quantity](CircularPatternFeatureInput_quantity.htm) | Gets and sets quantity of the elements. |
| [targetBaseFeature](CircularPatternFeatureInput_targetBaseFeature.htm) | When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.   Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it. |
| [totalAngle](CircularPatternFeatureInput_totalAngle.htm) | Gets and sets total angle. A negative angle can be used to reverse the direction. An angle of 360 degrees or 2 pi radians will create a full circular pattern. |

## Accessed From

[CircularPatternFeatures.createInput](CircularPatternFeatures_createInput.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [CircularPattern Feature API Sample](CircularPatternFeatureSample_Sample.htm) | Demonstrates creating a new circular pattern feature. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |