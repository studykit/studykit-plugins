# DocumentStockMaterialLibrary Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/StockMaterials/DocumentStockMaterialLibrary.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

DocumentStockMaterialLibrary provides access to stock materials used by the document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](DocumentStockMaterialLibrary_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](DocumentStockMaterialLibrary_item.htm) | Get StockMaterial by index in DocumentStockMaterialLibrary. |
| [setupsByStockMaterial](DocumentStockMaterialLibrary_setupsByStockMaterial.htm) | Returns all setups that use the given StockMaterial. The StockMaterial must exist in the document StockMaterial library. Raises an error if the StockMaterial is not in the document. |
| [update](DocumentStockMaterialLibrary_update.htm) | Update the given StockMaterial in the document StockMaterial library. The update applies all changes to the stockMaterial in the document stockMaterial library and therefore on all setups that use the stockMaterial. Will error if the stockMaterial does not exist in the document stockMaterial library. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](DocumentStockMaterialLibrary_count.htm) | The number of StockMaterial in the DocumentStockMaterialLibrary. |
| [isValid](DocumentStockMaterialLibrary_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](DocumentStockMaterialLibrary_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CAM.documentStockMaterialLibrary](CAM_documentStockMaterialLibrary.htm)

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |