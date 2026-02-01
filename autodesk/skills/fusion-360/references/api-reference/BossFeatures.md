# BossFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeatures.h>

## Description

Collection that provides access to all of the existing boss features in a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](BossFeatures_add.htm) | Creates a new boss feature (or more boss features) based on the information provided by a BossFeatureInput object. To create a new boss or boss connection, use createInput function to define a new input object for the type of boss feature you want to create. Use the methods and properties on the input object to define any additional inputs. Once the information is defined on the input object, you can pass it to the Add method to create the boss feature or boss connection. |
| [classType](BossFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](BossFeatures_createInput.htm) | Creates a new BossFeatureInput object that is used to specify the input needed to create a new boss feature(s). |
| [item](BossFeatures_item.htm) | Function that returns the specified boss feature using an index into the collection. |
| [itemByName](BossFeatures_itemByName.htm) | Function that returns the specified boss feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](BossFeatures_count.htm) | The number of boss features in the collection. |
| [isValid](BossFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BossFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.bossFeatures](Features_bossFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Boss Feature Sample](BossFeatureSample_Sample.htm) | Demonstrates creating a new boss feature |

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |