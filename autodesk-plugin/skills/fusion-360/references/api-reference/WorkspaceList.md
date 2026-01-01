# WorkspaceList Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/WorkspaceList.h>

## Description

A WorkspaceList is a list of Workspaces - e.g. the Workspaces for a given product.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](WorkspaceList_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](WorkspaceList_item.htm) | Returns the specified work space using an index into the collection. |
| [itemById](WorkspaceList_itemById.htm) | Returns the Workspace of the specified ID. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](WorkspaceList_count.htm) | Gets the number of workspaces in the collection. |
| [isValid](WorkspaceList_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](WorkspaceList_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CAM.workspaces](CAM_workspaces.htm), [Design.workspaces](Design_workspaces.htm), [Drawing.workspaces](Drawing_workspaces.htm), [FlatPatternProduct.workspaces](FlatPatternProduct_workspaces.htm), [Product.workspaces](Product_workspaces.htm), [UserInterface.workspacesByProductType](UserInterface_workspacesByProductType.htm), [WorkingModel.workspaces](WorkingModel_workspaces.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |