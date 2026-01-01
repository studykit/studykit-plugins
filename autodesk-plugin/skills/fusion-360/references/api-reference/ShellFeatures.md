# ShellFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeatures.h>

## Description

Collection that provides access to all of the existing shell features in a component and supports the ability to create new shell features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](ShellFeatures_add.htm) | Creates a new shell feature. |
| [classType](ShellFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](ShellFeatures_createInput.htm) | Creates a ShellFeatureInput object. Use properties and methods on this object to define the shell you want to create and then use the Add method, passing in the ShellFeatureInput object. |
| [item](ShellFeatures_item.htm) | Function that returns the specified shell feature using an index into the collection. |
| [itemByName](ShellFeatures_itemByName.htm) | Function that returns the specified shell feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ShellFeatures_count.htm) | The number of shell features in the collection. |
| [isValid](ShellFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ShellFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.shellFeatures](Features_shellFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Shell Feature API Sample](ShellFeatureSample_Sample.htm) | Demonstrates creating a new shell feature. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |