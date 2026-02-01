# Material Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Materials/Material.h>

## Description

A material.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Material_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copyTo](Material_copyTo.htm) | \*\*RETIRED\*\* Copies this material to the specified target. |
| [deleteMe](Material_deleteMe.htm) | Deletes the material from the Design. This method only applies to materials in a Design that are unused |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [appearance](Material_appearance.htm) | Gets the Appearance of this material. |
| [description](Material_description.htm) | Gets and sets the description associated with this material. Setting the description is only valid for materials in a document or the favorites list. |
| [id](Material_id.htm) | Returns the unique internal ID of this material. |
| [isUsed](Material_isUsed.htm) | Returns true if this material is used in the Design |
| [isValid](Material_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [materialProperties](Material_materialProperties.htm) | Returns the collection of material properties associated with this material. |
| [name](Material_name.htm) | Returns the name of this Material. This is the name of the material as seen in the user interface. The name can only be edited if the material is in a Design or the favorites list. |
| [objectType](Material_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parent](Material_parent.htm) | Returns the Parent object (a Library or a Design). |

## Accessed From

[BRepBody.material](BRepBody_material.htm), [Component.material](Component_material.htm), [ConfigurationMaterialCell.material](ConfigurationMaterialCell_material.htm), [FavoriteMaterials.add](FavoriteMaterials_add.htm), [FavoriteMaterials.item](FavoriteMaterials_item.htm), [FavoriteMaterials.itemById](FavoriteMaterials_itemById.htm), [FavoriteMaterials.itemByName](FavoriteMaterials_itemByName.htm), [FlatPatternComponent.material](FlatPatternComponent_material.htm), [Material.copyTo](Material_copyTo.htm), [MaterialPreferences.defaultMaterial](MaterialPreferences_defaultMaterial.htm), [Materials.addByCopy](Materials_addByCopy.htm), [Materials.item](Materials_item.htm), [Materials.itemById](Materials_itemById.htm), [Materials.itemByName](Materials_itemByName.htm), [MeshBody.material](MeshBody_material.htm), [PlasticRule.material](PlasticRule_material.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |