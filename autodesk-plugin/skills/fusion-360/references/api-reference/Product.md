# Product Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/Product.h>

## Description

The base class for the various product specific containers. For Fusion this is the Design object. For manufacturing this is a CAM object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Product_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteEntities](Product_deleteEntities.htm) | Deletes the specified set of entities that are associated with this product. |
| [findAttributes](Product_findAttributes.htm) | Find attributes attached to objects in this product that match the group and or attribute name. This does not find attributes attached directly to the Product or Document objects but finds the attributes attached to entities within the product. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [attributes](Product_attributes.htm) | Returns the collection of attributes associated with this product. |
| [isValid](Product_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [namedViews](Product_namedViews.htm) | Returns the NamedViews object associated with this product. The NamedViews collection provides access to the named views defined in this product and supports the creation of new named views. |
| [objectType](Product_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentDocument](Product_parentDocument.htm) | Returns the parent Document object. |
| [productType](Product_productType.htm) | Returns the product type name of this product. A list of all of the possible product types can be obtained by using the Application.supportedProductTypes property. |
| [selectionSets](Product_selectionSets.htm) | Returns the SelectionSets object associated with this product. If the product does not support selection sets, null is returned. The SelectionSets object is used to create and access existing selection sets. |
| [unitsManager](Product_unitsManager.htm) | Returns the UnitsManager object associated with this product. |
| [workspaces](Product_workspaces.htm) | Returns the workspaces associated with this product. |

## Accessed From

[Application.activeProduct](Application_activeProduct.htm), [FusionUnitsManager.product](FusionUnitsManager_product.htm), [NamedView.parentProduct](NamedView_parentProduct.htm), [Products.item](Products_item.htm), [Products.itemByProductType](Products_itemByProductType.htm), [RenderManager.parentDesign](RenderManager_parentDesign.htm), [UnitsManager.product](UnitsManager_product.htm)

## Derived Classes

[CAM](CAM.htm), [Design](Design.htm), [Drawing](Drawing.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Simple Extrusion Sample](SimpleExtrusionSample_Sample.htm) | Creates a new extrusion feature, resulting in a new component. |
| [Simple Revolve Feature Sample](SimpleRevolveFeatureSample_Sample.htm) | Creates a new revolve feature, resulting in a new component. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |