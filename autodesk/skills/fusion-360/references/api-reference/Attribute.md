# Attribute Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/Attribute.h>

## Description

Represents an attribute associated with a specific entity, Product, or Document. An attribute is a named value.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Attribute_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](Attribute_deleteMe.htm) | Deletes this attribute. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [groupName](Attribute_groupName.htm) | Gets the name of the group this attribute is a part of. |
| [isValid](Attribute_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](Attribute_name.htm) | Gets the name of the attribute. |
| [objectType](Attribute_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [otherParents](Attribute_otherParents.htm) | In the case where the entity the attribute was originally placed on has been split, this property will return the other entities the attribute is associated with. For example, if an attribute is placed on a face and then a slot is created that cuts the face into two pieces and the attribute is available from both faces. The parent property returns the "primary" entity and this property returns any other entities, if any. If there aren't any other associated entities the ObjectCollection returned will be empty. |
| [parent](Attribute_parent.htm) | Returns the parent entity this attribute is associated with. This can return null in some cases. For example a BRepEdge might have been consumed by a fillet feature but can come back if the model is rolled back or the fillet is deleted.   It's possible that the original parent that an attribute was placed on has been split. For example, if an attribute is placed on a face and then a slot is created that cuts the face into two pieces and the attribute is available from each face. In this case the parent property will return the "primary" face, which in most cases is somewhat arbitrary. You can get the other entities the attribute is associated with by using the otherParents property. |
| [value](Attribute_value.htm) | Gets and sets the value of this attribute.   The size of an attribute value is limited to 2MB (2097152 bytes). If you need to save data that is larger than 2MB you'll need to break the data into pieces and save it in multiple attributes. |

## Accessed From

[Attributes.add](Attributes_add.htm), [Attributes.item](Attributes_item.htm), [Attributes.itemByName](Attributes_itemByName.htm), [Attributes.itemsByGroup](Attributes_itemsByGroup.htm), [CAM.findAttributes](CAM_findAttributes.htm), [Design.findAttributes](Design_findAttributes.htm), [Drawing.findAttributes](Drawing_findAttributes.htm), [FlatPatternProduct.findAttributes](FlatPatternProduct_findAttributes.htm), [Product.findAttributes](Product_findAttributes.htm), [WorkingModel.findAttributes](WorkingModel_findAttributes.htm)

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |