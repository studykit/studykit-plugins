# ProfilePathProxy Object

Derived from: [ProfilePath](../ProfilePath/ProfilePath.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ProfilePathProxy/ProfilePathProxy_Delete.md) | Method that deletes this ProfilePath object. This method can be used to delete profile paths that represent a set of connected curves as well as profile paths that represent text boxes. |
| [GetReferenceKey](../ProfilePathProxy/ProfilePathProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AddsMaterial](../ProfilePathProxy/ProfilePathProxy_AddsMaterial.md) | Gets or sets a Boolean indicating whether the path adds or removes material from the entire area. |
| [Application](../ProfilePathProxy/ProfilePathProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ProfilePathProxy/ProfilePathProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Closed](../ProfilePathProxy/ProfilePathProxy_Closed.md) | Property that returns a Boolean indicating if the path is closed or not. Returns True in the case of a closed path. This property is only valid if the profile path denotes a set of connected curves. On the other hand, if the profile path denotes a text box, which will be indicated by the value of the TextPath property being True, then this property does not apply. |
| [ContainingOccurrence](../ProfilePathProxy/ProfilePathProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Count](../ProfilePathProxy/ProfilePathProxy_Count.md) | Property that returns the number of items in this collection. This property is only valid if the profile path denotes a set of connected curves. On the other hand, if the profile path denotes a text box, which will be indicated by the value of the TextPath property being True, then this property does not apply. |
| [Item](../ProfilePathProxy/ProfilePathProxy_Item.md) | Returns the specified ProfileEntity object from the collection. This property is only valid if the profile path denotes a set of connected curves. On the other hand, if the profile path denotes a text box, which will be indicated by the value of the TextPath property being True, then this property does not apply. |
| [NativeObject](../ProfilePathProxy/ProfilePathProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../ProfilePathProxy/ProfilePathProxy_Parent.md) | Property that returns the parent Profile. |
| [TextBox](../ProfilePathProxy/ProfilePathProxy_TextBox.md) | Property that gets the text box this profile path was derived from. This property is only valid if the profile path denotes a text box which will be indicated by the value of the TextPath property being True. On the other hand, if the profile path denotes a set of connected curves, then this property does not apply and will return Nothing. |
| [TextBoxPath](../ProfilePathProxy/ProfilePathProxy_TextBoxPath.md) | Property that returns a Boolean indicating if the profile path denotes a text box. Returns True in the case that the path denotes a text box. If the profile path denotes a set of connected curves, then this property will return False. |
| [Type](../ProfilePathProxy/ProfilePathProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 6
