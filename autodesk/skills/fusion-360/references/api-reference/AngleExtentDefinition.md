# AngleExtentDefinition Object

Derived from: [ExtentDefinition](ExtentDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/AngleExtentDefinition.h>

## Description

Defines the inputs for an AngleExtentDefinition object. This feature extent is defined by an angle as well as whether the extent is symmetric or only in one direction. If the extent is not symmetric, a positive or negative angle can be used to control the direction.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](AngleExtentDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [angle](AngleExtentDefinition_angle.htm) | Gets the ModelParameter that defines the angle. The value of the angle can be edited by using the properties on the ModelParameter object to edit the parameter. |
| [isSymmetric](AngleExtentDefinition_isSymmetric.htm) | Gets and sets if the angle extent is in one direction or symmetric. For a hole this property will always return false and setting it is ignored. |
| [isValid](AngleExtentDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](AngleExtentDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentFeature](AngleExtentDefinition_parentFeature.htm) | Returns the parent feature that this definition is associated with. If this definition has been created statically and is not associated with a feature this property will return null. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |