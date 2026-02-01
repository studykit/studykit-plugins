# ProfilePlaneStartDefinition Object

Derived from: [ExtentDefinition](ExtentDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ProfilePlaneStartDefinition.h>

## Description

A definition object that is used to define a feature whose start plane is the sketch plane of the profile.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ProfilePlaneStartDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](ProfilePlaneStartDefinition_create.htm) | Statically creates a new ProfilePlaneStartDefinition object. This is used as input when creating a new feature and defining the starting condition. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ProfilePlaneStartDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ProfilePlaneStartDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentFeature](ProfilePlaneStartDefinition_parentFeature.htm) | Returns the parent feature that this definition is associated with. If this definition has been created statically and is not associated with a feature this property will return null. |
| [profilePlane](ProfilePlaneStartDefinition_profilePlane.htm) | Returns the geometric definition of the profile plane. |

## Accessed From

[ProfilePlaneStartDefinition.create](ProfilePlaneStartDefinition_create.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [extrudeFeatures.add using thin extrude](extrudeFeaturesThin_add_Sample.htm) | Demonstrates the extrudeFeatures.add method using the setThinExtrude method. To use this sample have a design open that contains a sketch with a profile. When you run the script you will be prompted to select the profile that will be used to create the thin extrusion. |

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |