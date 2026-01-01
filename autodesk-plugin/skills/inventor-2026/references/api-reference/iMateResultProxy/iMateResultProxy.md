# iMateResultProxy Object

Derived from: [iMateResult](../iMateResult/iMateResult.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../iMateResultProxy/iMateResultProxy_Delete.md) | Method that deletes the iMateResult. This method will fail if the iMateResult is a part of a composite iMateResult. |
| [GetInputs](../iMateResultProxy/iMateResultProxy_GetInputs.md) | Method that returns the input entities that were used to create this iMateResult object. |
| [GetReferenceKey](../iMateResultProxy/iMateResultProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetInputs](../iMateResultProxy/iMateResultProxy_SetInputs.md) | Method that edits the inputs of an iMate result. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AttributeSets](../iMateResultProxy/iMateResultProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Constraints](../iMateResultProxy/iMateResultProxy_Constraints.md) | Property that returns an AssemblyConstraintstEnumerator containing the constraints associated with this iMate. If the iMate is not a composite iMate this collection will contain one constraint. If it is a composite it can contain any number of constraints. |
| [ContainingOccurrence](../iMateResultProxy/iMateResultProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [IsComposite](../iMateResultProxy/iMateResultProxy_IsComposite.md) | Property that indicates if this iMateResult represents a composite iMate result. |
| [Name](../iMateResultProxy/iMateResultProxy_Name.md) | Gets and sets the name of the iMateResult. |
| [NativeObject](../iMateResultProxy/iMateResultProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [ParentComposite](../iMateResultProxy/iMateResultProxy_ParentComposite.md) | Property that returns the parent iMateResult object. This property is only valid in the case when the iMateResult object it is being called from is not a composite. This can be checked for by using the IsComposite property of the iMateResult object. |
| [Results](../iMateResultProxy/iMateResultProxy_Results.md) | Property that returns an iMateResultsEnumerator object that provides access to the iMate results object that are part of a composite iMate. This property is only valid in the case when the iMateResult object it is being called from is a composite. This can be checked for by using the IsComposite property of the iMateResult object. |
| [Suppressed](../iMateResultProxy/iMateResultProxy_Suppressed.md) | Gets and sets whether the iMateResult is suppressed or not. |
| [Type](../iMateResultProxy/iMateResultProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 11
