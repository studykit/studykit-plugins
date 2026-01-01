# RevolveFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeatures.h>

## Description

Collection that provides access to all of the existing revolve features in a design and supports the ability to create new revolve features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](RevolveFeatures_add.htm) | Creates a new revolve feature based on the information provided by the provided RevolveFeatureInput object. To create a new revolve, use the createInput function to create a new input object and then use the methods and properties on that object to define the required input for a revolve. Once the information is defined on the input object you can pass it to the Add method to create the revolve. |
| [classType](RevolveFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](RevolveFeatures_createInput.htm) | Creates a new RevolveFeatureInput object that is used to specify the input needed to create a new revolve feature. |
| [item](RevolveFeatures_item.htm) | Function that returns the specified revolve feature using an index into the collection. |
| [itemByName](RevolveFeatures_itemByName.htm) | Function that returns the specified revolve feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](RevolveFeatures_count.htm) | The number of revolve features in the collection. |
| [isValid](RevolveFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](RevolveFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.revolveFeatures](Features_revolveFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Simple Revolve Feature Sample](SimpleRevolveFeatureSample_Sample.htm) | Creates a new revolve feature, resulting in a new component. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |