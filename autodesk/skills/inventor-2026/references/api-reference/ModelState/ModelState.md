# ModelState Object

## Description

ModelState Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Activate](../ModelState/ModelState_Activate.md) | Method that activates the model state. |
| [Copy](../ModelState/ModelState_Copy.md) | Method that creates a copy of the ModelState. The new created ModelState is returned. |
| [CopyComponentSuppressionToVisibility](../ModelState/ModelState_CopyComponentSuppressionToVisibility.md) | Method that creates a new design view representation based on the suppression of components as defined by this model state. The newly created DesignViewRepresentation is returned. |
| [Delete](../ModelState/ModelState_Delete.md) | Method that deletes the ModelState. The method returns an error if this is a built-in ModelState. |
| [GetReferenceKey](../ModelState/ModelState_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelState/ModelState_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ModelState/ModelState_AttributeSets.md) | Gets the Attribute Sets collection on this object. |
| [BOMDelegate](../ModelState/ModelState_BOMDelegate.md) | Read-only property that returns the ModelState which this ModelState's BOM is delegated to. |
| [Document](../ModelState/ModelState_Document.md) | Read-only property that returns the model state member Document that associates with this model state. |
| [FactoryDocument](../ModelState/ModelState_FactoryDocument.md) | Read-only property that returns the model state factory Document. If the model state factory document is not open, query this property will cause it open. |
| [ModelStateType](../ModelState/ModelState_ModelStateType.md) | Read-only property that returns the enum indicating the model state type. This can be kMasterModelState, kSubstituteModelState, or kCustomModelState. |
| [Name](../ModelState/ModelState_Name.md) | Read-write property that gets and sets the name of the ModelState. When setting the name, the name must be unique with respect to all other ModelState objects in the document, or an error will occur. Setting this property returns an error if this is a built-in. |
| [Parent](../ModelState/ModelState_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [SubstituteDocumentDescriptor](../ModelState/ModelState_SubstituteDocumentDescriptor.md) | Read-only property that returns the DocumentDescriptor of the document associated with the substitute occurrence. This property returns Nothing if the ModelState property returns anything but kSubstituteModelState. |
| [SubstituteOccurrence](../ModelState/ModelState_SubstituteOccurrence.md) | Read-only property that returns the ComponentOccurrence object associated with this model state. This property returns Nothing if the ModelState property returns anything but kSubstituteModelState. |
| [Type](../ModelState/ModelState_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[DesignViewRepresentation.CopyComponentVisibilityToSuppression](../DesignViewRepresentation/DesignViewRepresentation_CopyComponentVisibilityToSuppression.md), [ModelState.BOMDelegate](../ModelState/ModelState_BOMDelegate.md), [ModelState.Copy](../ModelState/ModelState_Copy.md), [ModelStates.ActiveModelState](../ModelStates/ModelStates_ActiveModelState.md), [ModelStates.Add](../ModelStates/ModelStates_Add.md), [ModelStates.AddSubstitute](../ModelStates/ModelStates_AddSubstitute.md), [ModelStates.Item](../ModelStates/ModelStates_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a model state](../../sample-programs/ModelStates_Add_Sample.md) | This sample demonstrates creation of a model state in an assembly. |
| [Shrink wrap substitute in assembly](../../sample-programs/Shrinkwrap_Sample.md) | The following sample demonstrates the creation of a shrinkwrap substitute within an assembly. |

## Version

Introduced in version 2022
