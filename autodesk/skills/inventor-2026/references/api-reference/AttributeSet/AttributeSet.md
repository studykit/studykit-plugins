# AttributeSet Object

## Description

The AttributeSet object provides the ability to create new attributes and access existing attributes. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../AttributeSet/AttributeSet_Add.md) | Method that creates a new attribute in the attribute set. The created Attribute object is returned. |
| [AddAttributes](../AttributeSet/AttributeSet_AddAttributes.md) | Adds attributes to the AttributeSet using the arrays that specify the names, valuetypes and values of the desired attributes |
| [CopyTo](../AttributeSet/AttributeSet_CopyTo.md) | Copies the Attribute Set to another object. Returns reference to the copied Attribute Set. |
| [Delete](../AttributeSet/AttributeSet_Delete.md) | Method that deletes this AttributeSet. |
| [GetReferenceKey](../AttributeSet/AttributeSet_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../AttributeSet/AttributeSet_Copy.md) | Gets the Boolean flag that indicates whether this set was created as a result of a operation that copied the owner Inventor Object. |
| [CopyWithOwner](../AttributeSet/AttributeSet_CopyWithOwner.md) | Gets the Boolean flag that controls the behavior of whether this set will copied onto this Inventor Object's copy. |
| [Count](../AttributeSet/AttributeSet_Count.md) | Property that returns the number of attributes within this attribute set. |
| [DataIO](../AttributeSet/AttributeSet_DataIO.md) | Property that returns the object that allows you to write the contents of the AttributeSet as XML. The DataIO object returned supports the WriteDataToFile method with the format "XML." The AttributeSet name is used as a tag name in the XML data. Because of this, the name must be a valid XML tag name. This means it must begin with a letter and can contain the following characters '\_', '-', '.'. Spaces are not allowed. |
| [Item](../AttributeSet/AttributeSet_Item.md) | Returns the specified Attribute object from the attribute set. This is the default property of the AttributeSet object. |
| [Name](../AttributeSet/AttributeSet_Name.md) | Gets/Sets the name of the Attribute Set. |
| [NameIsUsed](../AttributeSet/AttributeSet_NameIsUsed.md) | Property that returns whether an existing attribute has the specific name or not. Returns True if the name is already being used. |
| [Parent](../AttributeSet/AttributeSet_Parent.md) | Property that returns the Autodesk Inventor object being attributed with this AttributeSet. If this AttributeSet is being shared by more than one Autodesk Inventor object, then an ObjectCollection is returned that contains all of the Autodesk Inventor objects attributed with this AttributeSet. |
| [Transient](../AttributeSet/AttributeSet_Transient.md) | Gets the Boolean flag indicating whether this Attribute set is transient. (Meaning it is available only during this session). |
| [Type](../AttributeSet/AttributeSet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AttributeSet.CopyTo](../AttributeSet/AttributeSet_CopyTo.md), [AttributeSets.Add](../AttributeSets/AttributeSets_Add.md), [AttributeSets.AddTransient](../AttributeSets/AttributeSets_AddTransient.md), [AttributeSets.Item](../AttributeSets/AttributeSets_Item.md), [AttributeSetsEnumerator.Item](../AttributeSetsEnumerator/AttributeSetsEnumerator_Item.md)

## Version

Introduced in version 5
