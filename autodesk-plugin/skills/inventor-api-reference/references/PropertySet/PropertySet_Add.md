# PropertySet.Add Method

Parent Object: [PropertySet](../PropertySet/PropertySet.md)

## Description

Adds a new Property to this PropertySet.

## Syntax

PropertySet.**Add**( ***PropValue*** As Variant, [***Name***] As Variant, [***PropId***] As Variant ) As [Property](../Property/Property.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PropValue | Variant | Input Variant that specifies the value of the Property to add to the set. |
| Name | Variant | Input Variant that specifies the name of the Property. When add a property in a custom property set but not the built-in "User Defined Properties" set(whose internal name is {D5CDD505-2E9C-101B-9397-08002B2CF9AE}), if this name is prefixed with an "\_" character, then this property is created as a hidden property and can only be accessed if indexed by its name or propID. PropertySet.Count will not account for such hidden properties. |
| PropId | Variant | Input Variant that specifies the PropertyID of the Property to add to the set. Valid propids are 2 through 254 and 256 through 0x80000000. Other values are reserved.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create custom iProperties](../../sample-programs/iPropertyCreateCustom_Sample.md) | Creates custom iProperties of various types. A document must be open when this sample is run. |
| [Create or update custom iProperty](../../sample-programs/iPropertyCreateUpdateCustom_Sample.md) | This example creates a custom iProperty if it doesn't exist and updates the value if it does already exist. A part document must be open before runnin the sample. |

## Version

Introduced in version 4
