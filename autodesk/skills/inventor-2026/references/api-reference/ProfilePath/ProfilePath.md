# ProfilePath Object

## Description

The ProfilePath object represents a single set of connected curves or a text box. The order of the collection defines the connected order of the entities. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ProfilePath/ProfilePath_Delete.md) | Method that deletes this ProfilePath object. This method can be used to delete profile paths that represent a set of connected curves as well as profile paths that represent text boxes. |
| [GetReferenceKey](../ProfilePath/ProfilePath_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AddsMaterial](../ProfilePath/ProfilePath_AddsMaterial.md) | Gets or sets a Boolean indicating whether the path adds or removes material from the entire area. |
| [Application](../ProfilePath/ProfilePath_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ProfilePath/ProfilePath_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Closed](../ProfilePath/ProfilePath_Closed.md) | Property that returns a Boolean indicating if the path is closed or not. Returns True in the case of a closed path. This property is only valid if the profile path denotes a set of connected curves. On the other hand, if the profile path denotes a text box, which will be indicated by the value of the TextPath property being True, then this property does not apply. |
| [Count](../ProfilePath/ProfilePath_Count.md) | Property that returns the number of items in this collection. This property is only valid if the profile path denotes a set of connected curves. On the other hand, if the profile path denotes a text box, which will be indicated by the value of the TextPath property being True, then this property does not apply. |
| [Item](../ProfilePath/ProfilePath_Item.md) | Returns the specified ProfileEntity object from the collection. This property is only valid if the profile path denotes a set of connected curves. On the other hand, if the profile path denotes a text box, which will be indicated by the value of the TextPath property being True, then this property does not apply. |
| [Parent](../ProfilePath/ProfilePath_Parent.md) | Property that returns the parent Profile. |
| [TextBox](../ProfilePath/ProfilePath_TextBox.md) | Property that gets the text box this profile path was derived from. This property is only valid if the profile path denotes a text box which will be indicated by the value of the TextPath property being True. On the other hand, if the profile path denotes a set of connected curves, then this property does not apply and will return Nothing. |
| [TextBoxPath](../ProfilePath/ProfilePath_TextBoxPath.md) | Property that returns a Boolean indicating if the profile path denotes a text box. Returns True in the case that the path denotes a text box. If the profile path denotes a set of connected curves, then this property will return False. |
| [Type](../ProfilePath/ProfilePath_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Profile.Item](../Profile/Profile_Item.md), [ProfileEntity.Parent](../ProfileEntity/ProfileEntity_Parent.md), [ProfileEntityProxy.Parent](../ProfileEntityProxy/ProfileEntityProxy_Parent.md), [ProfilePathProxy.NativeObject](../ProfilePathProxy/ProfilePathProxy_NativeObject.md), [ProfileProxy.Item](../ProfileProxy/ProfileProxy_Item.md)

## Derived Classes

[ProfilePathProxy](../ProfilePathProxy/ProfilePathProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch profile control](../../sample-programs/ProfilePath_AddsMaterial_Sample.md) | This sample demonstrates the usage of the Profiles API to control the shape of the profile. The sample creates three concntric circles and creates an extrusion of the region between the inner circles. |

## Version

Introduced in version 5
