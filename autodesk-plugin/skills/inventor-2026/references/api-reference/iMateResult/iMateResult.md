# iMateResult Object

## Description

The iMateResult object represents the result of using an iMate in an assembly.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../iMateResult/iMateResult_Delete.md) | Method that deletes the iMateResult. This method will fail if the iMateResult is a part of a composite iMateResult. |
| [GetInputs](../iMateResult/iMateResult_GetInputs.md) | Method that returns the input entities that were used to create this iMateResult object. |
| [GetReferenceKey](../iMateResult/iMateResult_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetInputs](../iMateResult/iMateResult_SetInputs.md) | Method that edits the inputs of an iMate result. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AttributeSets](../iMateResult/iMateResult_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Constraints](../iMateResult/iMateResult_Constraints.md) | Property that returns an AssemblyConstraintstEnumerator containing the constraints associated with this iMate. If the iMate is not a composite iMate this collection will contain one constraint. If it is a composite it can contain any number of constraints. |
| [IsComposite](../iMateResult/iMateResult_IsComposite.md) | Property that indicates if this iMateResult represents a composite iMate result. |
| [Name](../iMateResult/iMateResult_Name.md) | Gets and sets the name of the iMateResult. |
| [ParentComposite](../iMateResult/iMateResult_ParentComposite.md) | Property that returns the parent iMateResult object. This property is only valid in the case when the iMateResult object it is being called from is not a composite. This can be checked for by using the IsComposite property of the iMateResult object. |
| [Results](../iMateResult/iMateResult_Results.md) | Property that returns an iMateResultsEnumerator object that provides access to the iMate results object that are part of a composite iMate. This property is only valid in the case when the iMateResult object it is being called from is a composite. This can be checked for by using the IsComposite property of the iMateResult object. |
| [Suppressed](../iMateResult/iMateResult_Suppressed.md) | Gets and sets whether the iMateResult is suppressed or not. |
| [Type](../iMateResult/iMateResult_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AngleConstraint.iMateResult](../AngleConstraint/AngleConstraint_iMateResult.md), [AngleConstraintProxy.iMateResult](../AngleConstraintProxy/AngleConstraintProxy_iMateResult.md), [AssemblyConstraint.iMateResult](../AssemblyConstraint/AssemblyConstraint_iMateResult.md), [AssemblySymmetryConstraint.iMateResult](../AssemblySymmetryConstraint/AssemblySymmetryConstraint_iMateResult.md), [AssemblySymmetryConstraintProxy.iMateResult](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_iMateResult.md), [CustomConstraint.iMateResult](CustomConstraint_iMateResult.md), [CustomConstraintProxy.iMateResult](CustomConstraintProxy_iMateResult.md), [FlushConstraint.iMateResult](../FlushConstraint/FlushConstraint_iMateResult.md), [FlushConstraintProxy.iMateResult](../FlushConstraintProxy/FlushConstraintProxy_iMateResult.md), [iMateResult.ParentComposite](../iMateResult/iMateResult_ParentComposite.md), [iMateResultProxy.NativeObject](../iMateResultProxy/iMateResultProxy_NativeObject.md), [iMateResultProxy.ParentComposite](../iMateResultProxy/iMateResultProxy_ParentComposite.md), [iMateResults.AddByiMateAndEntity](../iMateResults/iMateResults_AddByiMateAndEntity.md), [iMateResults.AddByTwoiMates](../iMateResults/iMateResults_AddByTwoiMates.md), [iMateResults.Item](../iMateResults/iMateResults_Item.md), [iMateResultsEnumerator.Item](../iMateResultsEnumerator/iMateResultsEnumerator_Item.md), [InsertConstraint.iMateResult](../InsertConstraint/InsertConstraint_iMateResult.md), [InsertConstraintProxy.iMateResult](../InsertConstraintProxy/InsertConstraintProxy_iMateResult.md), [MateConstraint.iMateResult](../MateConstraint/MateConstraint_iMateResult.md), [MateConstraintProxy.iMateResult](../MateConstraintProxy/MateConstraintProxy_iMateResult.md), [RotateRotateConstraint.iMateResult](../RotateRotateConstraint/RotateRotateConstraint_iMateResult.md), [RotateRotateConstraintProxy.iMateResult](../RotateRotateConstraintProxy/RotateRotateConstraintProxy_iMateResult.md), [RotateTranslateConstraint.iMateResult](../RotateTranslateConstraint/RotateTranslateConstraint_iMateResult.md), [RotateTranslateConstraintProxy.iMateResult](../RotateTranslateConstraintProxy/RotateTranslateConstraintProxy_iMateResult.md), [TangentConstraint.iMateResult](../TangentConstraint/TangentConstraint_iMateResult.md), [TangentConstraintProxy.iMateResult](../TangentConstraintProxy/TangentConstraintProxy_iMateResult.md), [TransitionalConstraint.iMateResult](../TransitionalConstraint/TransitionalConstraint_iMateResult.md), [TransitionalConstraintProxy.iMateResult](../TransitionalConstraintProxy/TransitionalConstraintProxy_iMateResult.md), [TranslateTranslateConstraint.iMateResult](../TranslateTranslateConstraint/TranslateTranslateConstraint_iMateResult.md), [TranslateTranslateConstraintProxy.iMateResult](../TranslateTranslateConstraintProxy/TranslateTranslateConstraintProxy_iMateResult.md)

## Derived Classes

[iMateResultProxy](../iMateResultProxy/iMateResultProxy.md)

## Version

Introduced in version 6
