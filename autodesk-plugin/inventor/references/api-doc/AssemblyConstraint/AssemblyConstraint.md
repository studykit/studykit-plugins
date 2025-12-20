# AssemblyConstraint Object

## Description

Object that represents the base class of an assembly constraint.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToAngleConstraint](../AssemblyConstraint/AssemblyConstraint_ConvertToAngleConstraint.md) | Method that converts the constraint to an angle constraint, and returns the AngleConstraint object. This method can also be used to edit the geometries associated with an angle constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToCustomConstraint](../AssemblyConstraint/AssemblyConstraint_ConvertToCustomConstraint.md) | Method that converts the constraint to a custom constraint, and returns the CustomConstraint object. This method can also be used to edit the geometries associated with a custom constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToFlushConstraint](../AssemblyConstraint/AssemblyConstraint_ConvertToFlushConstraint.md) | Method that converts the constraint to a flush constraint, and returns the FlushConstraint object. This method can also be used to edit the geometries associated with a flush constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToInsertConstraint](../AssemblyConstraint/AssemblyConstraint_ConvertToInsertConstraint.md) | Method that converts the constraint to an insert constraint, and returns the InsertConstraint object. This method can also be used to edit the geometries associated with an insert constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToInsertConstraint2](../AssemblyConstraint/AssemblyConstraint_ConvertToInsertConstraint2.md) | Converts the constraint to an insert constraint, and returns the InsertConstraint object. |
| [ConvertToMateConstraint](../AssemblyConstraint/AssemblyConstraint_ConvertToMateConstraint.md) | Method that converts the constraint to a mate constraint, and returns the MateConstraint object. This method can also be used to edit the geometries associated with a mate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToMateConstraint2](../AssemblyConstraint/AssemblyConstraint_ConvertToMateConstraint2.md) | Converts the constraint to a mate constraint, and returns the MateConstraint object. |
| [ConvertToRotateRotateConstraint](../AssemblyConstraint/AssemblyConstraint_ConvertToRotateRotateConstraint.md) | Method that converts the constraint to a rotate-rotate constraint, and returns the RotateRotateConstraint object. This method can also be used to edit the geometries associated with a rotate-rotate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToRotateTranslateConstraint](../AssemblyConstraint/AssemblyConstraint_ConvertToRotateTranslateConstraint.md) | Method that converts the constraint to a rotate-translate constraint, and returns the RotateTranslateConstraint object. This method can also be used to edit the geometries associated with a rotate-translate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToSymmetryConstraint](../AssemblyConstraint/AssemblyConstraint_ConvertToSymmetryConstraint.md) | Converts the constraint to a symmetry constraint, and returns the AssemblySymmetryConstraint object. |
| [ConvertToTangentConstraint](../AssemblyConstraint/AssemblyConstraint_ConvertToTangentConstraint.md) | Method that converts the constraint to a tangent constraint, and returns the TangentConstraint object. This method can also be used to edit the geometries associated with a tangent constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToTransitionalConstraint](../AssemblyConstraint/AssemblyConstraint_ConvertToTransitionalConstraint.md) | Method that converts the constraint to a transitional constraint, and returns the TransitionalConstraint object. This method can also be used to edit the geometries associated with a transitional constraint without changing its type, in which case the same object is returned by the method. |
| [Delete](../AssemblyConstraint/AssemblyConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../AssemblyConstraint/AssemblyConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedOccurrenceOne](../AssemblyConstraint/AssemblyConstraint_AffectedOccurrenceOne.md) | Property that returns the first of the two objects affected by this constraint. This is the same as the owning occurrence obtained from the OccurrenceOne property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the first of the two geometries that this constraint is between. |
| [AffectedOccurrenceTwo](../AssemblyConstraint/AssemblyConstraint_AffectedOccurrenceTwo.md) | Property that returns the second of the two objects affected by this constraint. This is the same as the owning occurrence obtained from the OccurrenceTwo property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the second of the two geometries that this constraint is between. |
| [Application](../AssemblyConstraint/AssemblyConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../AssemblyConstraint/AssemblyConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DriveSettings](../AssemblyConstraint/AssemblyConstraint_DriveSettings.md) | Returns the DriveSettings object for the constraint. |
| [EntityOne](../AssemblyConstraint/AssemblyConstraint_EntityOne.md) | Property that indicates the first of the geometric entities (Face, Axis, Edge, etc.) being constrained. |
| [EntityTwo](../AssemblyConstraint/AssemblyConstraint_EntityTwo.md) | Property that indicates the second of the geometric entities (Face, Axis, Edge, etc.) being constrained. |
| [GeometryOne](../AssemblyConstraint/AssemblyConstraint_GeometryOne.md) | Property that returns the geometry of the first of the two entities that this constraint is between. The geometry returned is in the space of the assembly and for face or work plane geometries it accounts for the orientation of the face or work plane. |
| [GeometryTwo](../AssemblyConstraint/AssemblyConstraint_GeometryTwo.md) | Property that returns the geometry of the second of the two entities that this constraint is between. The geometry returned is in the space of the assembly and for face or work plane geometries it accounts for the orientation of the face or work plane. |
| [HealthStatus](../AssemblyConstraint/AssemblyConstraint_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [iMateResult](../AssemblyConstraint/AssemblyConstraint_iMateResult.md) | Property that returns the iMateResult object that resulted in the creation of this constraint. |
| [IsDefaultName](../AssemblyConstraint/AssemblyConstraint_IsDefaultName.md) | Indicates if the name of this constraint is the original default name or if the user has changed the name. A value of True indicates the name is the original default name. |
| [LayoutConstraint](../AssemblyConstraint/AssemblyConstraint_LayoutConstraint.md) | Property that returns the layout constraint this constraint is a member of. Returns Nothing in the case where this constraint is not a member of a layout constraint. You can also determine if a constraint is a member of a layout constraint by using the ResultOfLayoutConstraint property. |
| [Name](../AssemblyConstraint/AssemblyConstraint_Name.md) | Gets/Sets the displayable name of this constraint. |
| [OccurrenceOne](../AssemblyConstraint/AssemblyConstraint_OccurrenceOne.md) | Property that returns the first of the two objects this constraint is between. |
| [OccurrenceTwo](../AssemblyConstraint/AssemblyConstraint_OccurrenceTwo.md) | Property that returns the second of the two objects this constraint is between. |
| [Parent](../AssemblyConstraint/AssemblyConstraint_Parent.md) | Property that returns the parent of the object. |
| [ResultOfiMate](../AssemblyConstraint/AssemblyConstraint_ResultOfiMate.md) | Property that indicates if this iMateResult represents a composite iMate. |
| [ResultOfLayoutConstraint](../AssemblyConstraint/AssemblyConstraint_ResultOfLayoutConstraint.md) | Property that indicates if this constraint is a member of a layout constraint. If True then it is a member of a layout constraint. The layout constraint can be obtained by using the LayoutConstraint property. |
| [Suppressed](../AssemblyConstraint/AssemblyConstraint_Suppressed.md) | Gets/Sets the Boolean flag indicating whether this constraint is suppressed. |
| [Type](../AssemblyConstraint/AssemblyConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../AssemblyConstraint/AssemblyConstraint_Visible.md) | Gets/Sets the Visible indicating whether this constraint is visible. |

## Accessed From

[AssemblyConstraints.Item](../AssemblyConstraints/AssemblyConstraints_Item.md), [AssemblyConstraintsEnumerator.Item](../AssemblyConstraintsEnumerator/AssemblyConstraintsEnumerator_Item.md), [DriveConstraintSettings.Parent](../DriveConstraintSettings/DriveConstraintSettings_Parent.md)

## Derived Classes

[AngleConstraint](../AngleConstraint/AngleConstraint.md), [AssemblySymmetryConstraint](../AssemblySymmetryConstraint/AssemblySymmetryConstraint.md), [FlushConstraint](../FlushConstraint/FlushConstraint.md), [InsertConstraint](../InsertConstraint/InsertConstraint.md), [MateConstraint](../MateConstraint/MateConstraint.md), [RotateRotateConstraint](../RotateRotateConstraint/RotateRotateConstraint.md), [RotateTranslateConstraint](../RotateTranslateConstraint/RotateTranslateConstraint.md), [TangentConstraint](../TangentConstraint/TangentConstraint.md), [TransitionalConstraint](../TransitionalConstraint/TransitionalConstraint.md), [TranslateTranslateConstraint](../TranslateTranslateConstraint/TranslateTranslateConstraint.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Assembly Ground Occurrences](../../sample-programs/ComponentOccurrence_Grounded_Sample.md) | This sample demonstrates grounding an assembly occurrence. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |