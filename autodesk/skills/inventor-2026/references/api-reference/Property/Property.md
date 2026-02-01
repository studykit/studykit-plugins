# Property Object

## Description

Object that represents a Property. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../Property/Property_Delete.md) | Method that deletes this Property from its PropertySet. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Dirty](../Property/Property_Dirty.md) | Property that returns a Boolean flag that indicates whether this property has been edited or created. |
| [DisplayName](../Property/Property_DisplayName.md) | Gets/Sets the human-readable name associated with this Property. |
| [Expression](../Property/Property_Expression.md) | Gets/Sets expression that defines the value of this property. |
| [Name](../Property/Property_Name.md) | Gets the human-readable name of this Property, if any. |
| [Parent](../Property/Property_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [PropId](../Property/Property_PropId.md) | Gets the identifier (PROPID) of this Property. |
| [Type](../Property/Property_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Value](../Property/Property_Value.md) | Gets/Sets the value of this Property. |

## Accessed From

[PropertySet.Add](../PropertySet/PropertySet_Add.md), [PropertySet.Item](../PropertySet/PropertySet_Item.md), [PropertySet.ItemByPropId](../PropertySet/PropertySet_ItemByPropId.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create or update custom iProperty](../../sample-programs/iPropertyCreateUpdateCustom_Sample.md) | This example creates a custom iProperty if it doesn't exist and updates the value if it does already exist. A part document must be open before runnin the sample. |
| [Get value of iProperty](../../sample-programs/iPropertyGetValue_Sample.md) | Demonstrates getting the values of the "Part Number" iProperty. Any property can be retrieved by accesing the correct property set and property.  A document must be open when this sample is run. |

## Version

Introduced in version 4
