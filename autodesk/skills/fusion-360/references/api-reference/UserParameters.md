# UserParameters Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/UserParameters.h>

## Description

Provides access to the User Parameters within a design and provides methods to create new user parameters.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](UserParameters_add.htm) | Adds a new user parameter to the collection. |
| [asArray](UserParameters_asArray.htm) | Returns the user parameters in the design as an array. |
| [classType](UserParameters_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [exportUserParameters](UserParameters_exportUserParameters.htm) | Function that exports a list of user parameters to a csv file. |
| [importUserParameters](UserParameters_importUserParameters.htm) | Function that imports a list of user parameters from a csv file. |
| [item](UserParameters_item.htm) | Function that returns the specified User Parameter using an index into the collection. |
| [itemByName](UserParameters_itemByName.htm) | Function that returns the specified User Parameter using the name of the parameter as it is displayed in the parameters dialog. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](UserParameters_count.htm) | Returns the number of parameters in the collection. |
| [design](UserParameters_design.htm) | Returns the design that owns the user parameters collection. |
| [isValid](UserParameters_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](UserParameters_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[Design.userParameters](Design_userParameters.htm), [FlatPatternProduct.userParameters](FlatPatternProduct_userParameters.htm), [UserParameter.userParameters](UserParameter_userParameters.htm), [WorkingModel.userParameters](WorkingModel_userParameters.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Set parameters from a csv file and export to STEP](SetParametersFromACsvFileAndExportToSTEP_Sample.htm) | Reads data from a .csv file and sets user parameters in the model and then exports the model to STEP. When setting parameters be aware that this sample is setting user parameters. It's also possible to set model parameters but that's not demonstrated here. Also when accessing parameters, it is case sensitive so the names you use in your program much exactly match the names in the model. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |