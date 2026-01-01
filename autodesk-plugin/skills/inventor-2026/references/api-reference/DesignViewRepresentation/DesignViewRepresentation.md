# DesignViewRepresentation Object

## Description

The DesignViewRepresentation object represents a design view representation in the assembly.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Activate](../DesignViewRepresentation/DesignViewRepresentation_Activate.md) | Method that activates the design view representation. |
| [Copy](../DesignViewRepresentation/DesignViewRepresentation_Copy.md) | Method that creates a copy of the DesignViewRepresentation. The new created DesignViewRepresentation is returned. |
| [CopyComponentVisibilityToSuppression](../DesignViewRepresentation/DesignViewRepresentation_CopyComponentVisibilityToSuppression.md) | Create a new ModelState based on the visibility of components as defined by the design view. The new created ModelState is returned. |
| [Delete](../DesignViewRepresentation/DesignViewRepresentation_Delete.md) | Method that deletes the DesignViewRepresentation. The method returns an error if the DesignViewType is kMasterDesignViewType. |
| [GetReferenceKey](../DesignViewRepresentation/DesignViewRepresentation_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSectionViewInfo](../DesignViewRepresentation/DesignViewRepresentation_GetSectionViewInfo.md) | Gets the current section view info in the design view. |
| [HideAll](../DesignViewRepresentation/DesignViewRepresentation_HideAll.md) | Method that makes all components invisible in this representation. |
| [RemoveAppearanceOverrides](../DesignViewRepresentation/DesignViewRepresentation_RemoveAppearanceOverrides.md) | Resets all components to their default appearance. |
| [RestoreCamera](../DesignViewRepresentation/DesignViewRepresentation_RestoreCamera.md) | Method that changes the camera of the active view to the camera stored with the design view. |
| [SaveCurrentCamera](../DesignViewRepresentation/DesignViewRepresentation_SaveCurrentCamera.md) | Method that saves the camera of the active view to the design view. |
| [SetAllContentCenterComponentsVisibility](../DesignViewRepresentation/DesignViewRepresentation_SetAllContentCenterComponentsVisibility.md) | Method that sets the visibility of all content center components. |
| [SetSectionView](../DesignViewRepresentation/DesignViewRepresentation_SetSectionView.md) | Sets a section view in the design view. |
| [SetVisibilityOfOccurrences](../DesignViewRepresentation/DesignViewRepresentation_SetVisibilityOfOccurrences.md) | Method that sets the visibility of a collection of occurrences. If occurrences within a subassembly are specified and the owning subassembly occurrence is associative to a design view representation, the associativity will be turned off. |
| [ShowAll](../DesignViewRepresentation/DesignViewRepresentation_ShowAll.md) | Method that makes all components visible in this representation. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DesignViewRepresentation/DesignViewRepresentation_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DesignViewRepresentation/DesignViewRepresentation_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AutoSaveCamera](../DesignViewRepresentation/DesignViewRepresentation_AutoSaveCamera.md) | Gets and sets weather the design view representations camera is saved automatically. |
| [Camera](../DesignViewRepresentation/DesignViewRepresentation_Camera.md) | Gets and sets the camera associated with this design view. |
| [DesignViewInfo](../DesignViewRepresentation/DesignViewRepresentation_DesignViewInfo.md) | Property that returns the design view representation information as a String containing XML formatted data. This is applicable for assembly documents only. For more information on the XML format see [More XML Design View Info...](MoreXMLDesignViewInfo_Overview.md) |
| [DesignViewType](../DesignViewRepresentation/DesignViewRepresentation_DesignViewType.md) | Property that returns the design view representation type. This can return kPrimaryDesignViewType, kPrivateDesignViewType, kPublicDesignViewType and kTransientDesignViewType. |
| [IsSectionViewSuppressed](../DesignViewRepresentation/DesignViewRepresentation_IsSectionViewSuppressed.md) | Gets and sets whether section view in this design view is suppressed or not. Set this to True will suppress the section view in this design view. The GetSectionViewInfo can be used to determine whether there is a section view or not. |
| [Locked](../DesignViewRepresentation/DesignViewRepresentation_Locked.md) | Gets and sets whether this design view representation is locked. If a representation is locked, changes made to it will not be saved to the document. Setting this property will fail if the DesignViewType is kMasterDesignViewType or kPrivateDesignViewType. |
| [ModelAnnotationAutoScale](../DesignViewRepresentation/DesignViewRepresentation_ModelAnnotationAutoScale.md) | Gets and sets the design view representations model annotation scale mode. |
| [ModelAnnotationScale](../DesignViewRepresentation/DesignViewRepresentation_ModelAnnotationScale.md) | Gets and sets the design view representations model annotation scale. |
| [Name](../DesignViewRepresentation/DesignViewRepresentation_Name.md) | Gets and sets the name of the DesignViewRepresentation. The name must be unique with respect to all other DesignViewRepresentation objects in the document, or an error will occur. Setting this property returns an error if the DesignViewType is kMasterDesignVi. |
| [Parent](../DesignViewRepresentation/DesignViewRepresentation_Parent.md) | Property that returns the parent RepresentationsManager object. |
| [Publish](../DesignViewRepresentation/DesignViewRepresentation_Publish.md) | Gets and sets whether this design view representation is published. |
| [Type](../DesignViewRepresentation/DesignViewRepresentation_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DesignViewRepresentation.Copy](../DesignViewRepresentation/DesignViewRepresentation_Copy.md), [DesignViewRepresentations.Add](../DesignViewRepresentations/DesignViewRepresentations_Add.md), [DesignViewRepresentations.Item](../DesignViewRepresentations/DesignViewRepresentations_Item.md), [ModelState.CopyComponentSuppressionToVisibility](../ModelState/ModelState_CopyComponentSuppressionToVisibility.md), [RepresentationsManager.ActiveDesignViewRepresentation](../RepresentationsManager/RepresentationsManager_ActiveDesignViewRepresentation.md)

## Version

Introduced in version 11
