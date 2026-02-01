# ClientNodeResource Object

## Description

This object is accessible through the BrowserPane. But it is in fact, just the one associated with the Document. In other words, all of the ClientNodeResource objects that are used inside the various BrowserPanes of this Document are to be found here.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ClientNodeResource/ClientNodeResource_Delete.md) | Method that gets rid of this object. If it is being used currently by some node definition object, the method fails. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ClientNodeResource/ClientNodeResource_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ClientId](../ClientNodeResource/ClientNodeResource_ClientId.md) | Property returning the string identifier that stood for the client or AddIn that was supplied during the creation of this resource. |
| [DisabledIconName](../ClientNodeResource/ClientNodeResource_DisabledIconName.md) | Gets and sets the icon name to be used when the associated data model object becomes disabled. |
| [ExpandedDisabledIconName](../ClientNodeResource/ClientNodeResource_ExpandedDisabledIconName.md) | Gets and sets the expanded icon name to be used when the associated data model objects becomes disabled. |
| [ExpandedInvisibleIconName](../ClientNodeResource/ClientNodeResource_ExpandedInvisibleIconName.md) | Gets and sets the expanded icon name to be used when the associated data model object becomes invisible. |
| [ExpandedSuppressedIconName](../ClientNodeResource/ClientNodeResource_ExpandedSuppressedIconName.md) | Gets and sets the expanded icon name to be used when the associated data model object becomes suppressed. |
| [GroundedDisabledIconName](../ClientNodeResource/ClientNodeResource_GroundedDisabledIconName.md) | Gets and sets the icon name to be used when the associated data model object becomes grounded and disabled. |
| [GroundedIconName](../ClientNodeResource/ClientNodeResource_GroundedIconName.md) | Gets and sets the icon name to be used when the associated data model object becomes grounded. |
| [GroundedInvisibleIconName](../ClientNodeResource/ClientNodeResource_GroundedInvisibleIconName.md) | Gets and sets the icon name to be used when the associated data model object becomes grounded and invisible. |
| [GroundedSuppressedIconName](../ClientNodeResource/ClientNodeResource_GroundedSuppressedIconName.md) | Gets and sets the icon name to be used when the associated data model object becomes grounded and suppressed. |
| [IconName](../ClientNodeResource/ClientNodeResource_IconName.md) | Gets and sets picture name associated with a ClientNodeResource object. |
| [Id](../ClientNodeResource/ClientNodeResource_Id.md) | Property returning the integer identifier that was supplied during the creation of this resource. |
| [InvisibleIconName](../ClientNodeResource/ClientNodeResource_InvisibleIconName.md) | Gets and sets the icon name to be used when the associated data model object becomes invisible. |
| [Parent](../ClientNodeResource/ClientNodeResource_Parent.md) | Property that returns the parent of this object. Though this document is reachable from the BrowserPane out of convenience, it's true parent is the Document itself. That is, this object is not BrowserPane specific, rather, it has its scope or influence across all BrowserPanes (of the TreeBrowser kind). |
| [SuppressedIconName](../ClientNodeResource/ClientNodeResource_SuppressedIconName.md) | Gets and sets the icon name to be used when the associated data model object becomes suppressed. |
| [Type](../ClientNodeResource/ClientNodeResource_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ClientBrowserNodeDefinition.ExpandedIcon](../ClientBrowserNodeDefinition/ClientBrowserNodeDefinition_ExpandedIcon.md), [ClientBrowserNodeDefinition.Icon](../ClientBrowserNodeDefinition/ClientBrowserNodeDefinition_Icon.md), [ClientNodeResources.AddNodeResource](../ClientNodeResources/ClientNodeResources_AddNodeResource.md), [ClientNodeResources.Item](../ClientNodeResources/ClientNodeResources_Item.md), [ClientNodeResources.ItemById](../ClientNodeResources/ClientNodeResources_ItemById.md), [NativeBrowserNodeDefinition.OverrideExpandedIcon](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_OverrideExpandedIcon.md), [NativeBrowserNodeDefinition.OverrideIcon](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_OverrideIcon.md), [NativeBrowserNodeDefinition.OverrideStateIcon](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_OverrideStateIcon.md)

## Version

Introduced in version 8
