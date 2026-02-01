# StockMaterial Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/StockMaterials/StockMaterial.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

Represents a StockMaterial.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](StockMaterial_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createFromJson](StockMaterial_createFromJson.htm) | Creates a StockMaterial object from given JSON string. |
| [toJson](StockMaterial_toJson.htm) | Generates and returns a JSON string that contains a description of this StockMaterial. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [category](StockMaterial_category.htm) | Gets and sets the category of the stock material. |
| [designators](StockMaterial_designators.htm) | Gets a list of designators of the stock material. |
| [hardness](StockMaterial_hardness.htm) | Get and sets the hardness of the stock materials. NOTE: the hardness can be NaN if not set. and user can set the hardness to NaN. |
| [isValid](StockMaterial_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](StockMaterial_name.htm) | Gets and sets the name of the stock material. |
| [objectType](StockMaterial_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[DocumentStockMaterialLibrary.item](DocumentStockMaterialLibrary_item.htm), [Setup.stockMaterial](Setup_stockMaterial.htm), [StockMaterial.createFromJson](StockMaterial_createFromJson.htm), [StockMaterialLibrary.childStockMaterials](StockMaterialLibrary_childStockMaterials.htm), [StockMaterialLibrary.stockMaterialAtURL](StockMaterialLibrary_stockMaterialAtURL.htm)

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |