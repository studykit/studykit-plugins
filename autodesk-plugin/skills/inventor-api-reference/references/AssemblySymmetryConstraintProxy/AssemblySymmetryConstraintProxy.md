# AssemblySymmetryConstraintProxy Object

Derived from: [AssemblySymmetryConstraint](../AssemblySymmetryConstraint/AssemblySymmetryConstraint.md) Object

## Description

AssemblySymmetryConstraintProxy object represents an AssemblySymmetryConstraint that was created in a subassembly within an assembly that contains that subassembly.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToAngleConstraint](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ConvertToAngleConstraint.md) | Method that converts the constraint to an angle constraint, and returns the AngleConstraint object. This method can also be used to edit the geometries associated with an angle constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToCustomConstraint](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ConvertToCustomConstraint.md) | Method that converts the constraint to a custom constraint, and returns the CustomConstraint object. This method can also be used to edit the geometries associated with a custom constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToFlushConstraint](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ConvertToFlushConstraint.md) | Method that converts the constraint to a flush constraint, and returns the FlushConstraint object. This method can also be used to edit the geometries associated with a flush constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToInsertConstraint](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ConvertToInsertConstraint.md) | Method that converts the constraint to an insert constraint, and returns the InsertConstraint object. This method can also be used to edit the geometries associated with an insert constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToInsertConstraint2](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ConvertToInsertConstraint2.md) | Converts the constraint to an insert constraint, and returns the InsertConstraint object. |
| [ConvertToMateConstraint](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ConvertToMateConstraint.md) | Method that converts the constraint to a mate constraint, and returns the MateConstraint object. This method can also be used to edit the geometries associated with a mate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToMateConstraint2](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ConvertToMateConstraint2.md) | Converts the constraint to a mate constraint, and returns the MateConstraint object. |
| [ConvertToRotateRotateConstraint](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ConvertToRotateRotateConstraint.md) | Method that converts the constraint to a rotate-rotate constraint, and returns the RotateRotateConstraint object. This method can also be used to edit the geometries associated with a rotate-rotate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToRotateTranslateConstraint](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ConvertToRotateTranslateConstraint.md) | Method that converts the constraint to a rotate-translate constraint, and returns the RotateTranslateConstraint object. This method can also be used to edit the geometries associated with a rotate-translate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToSymmetryConstraint](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ConvertToSymmetryConstraint.md) | Converts the constraint to a symmetry constraint, and returns the AssemblySymmetryConstraint object. |
| [ConvertToTangentConstraint](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ConvertToTangentConstraint.md) | Method that converts the constraint to a tangent constraint, and returns the TangentConstraint object. This method can also be used to edit the geometries associated with a tangent constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToTransitionalConstraint](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ConvertToTransitionalConstraint.md) | Method that converts the constraint to a transitional constraint, and returns the TransitionalConstraint object. This method can also be used to edit the geometries associated with a transitional constraint without changing its type, in which case the same object is returned by the method. |
| [Delete](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedOccurrenceOne](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_AffectedOccurrenceOne.md) | Property that returns the first of the two objects affected by this constraint. This is the same as the owning occurrence obtained from the OccurrenceOne property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the first of the two geometries that this constraint is between. |
| [AffectedOccurrenceTwo](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_AffectedOccurrenceTwo.md) | Property that returns the second of the two objects affected by this constraint. This is the same as the owning occurrence obtained from the OccurrenceTwo property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the second of the two geometries that this constraint is between. |
| [Application](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [DriveSettings](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_DriveSettings.md) | Returns the DriveSettings object for the constraint. |
| [EntityOne](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_EntityOne.md) | Property that indicates the first of the geometric entities (Face, Axis, Edge, etc.) being constrained. |
| [EntityOneInferredType](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_EntityOneInferredType.md) | Read-only property that returns an enum indicating how the geometry of entity one is interpreted. |
| [EntityTwo](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_EntityTwo.md) | Property that indicates the second of the geometric entities (Face, Axis, Edge, etc.) being constrained. |
| [EntityTwoInferredType](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_EntityTwoInferredType.md) | Read-only property that returns an enum indicating how the geometry of entity two is interpreted. |
| [GeometryOne](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_GeometryOne.md) | Property that returns the geometry of the first of the two entities that this constraint is between. The geometry returned is in the space of the assembly and for face or work plane geometries it accounts for the orientation of the face or work plane. |
| [GeometryTwo](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_GeometryTwo.md) | Property that returns the geometry of the second of the two entities that this constraint is between. The geometry returned is in the space of the assembly and for face or work plane geometries it accounts for the orientation of the face or work plane. |
| [HealthStatus](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [iMateResult](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_iMateResult.md) | Property that returns the iMateResult object that resulted in the creation of this constraint. |
| [IsDefaultName](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_IsDefaultName.md) | Indicates if the name of this constraint is the original default name or if the user has changed the name. A value of True indicates the name is the original default name. |
| [LayoutConstraint](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_LayoutConstraint.md) | Property that returns the layout constraint this constraint is a member of. Returns Nothing in the case where this constraint is not a member of a layout constraint. You can also determine if a constraint is a member of a layout constraint by using the ResultOfLayoutConstraint property. |
| [Name](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_Name.md) | Gets/Sets the displayable name of this constraint. |
| [NativeObject](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [NormalsOpposed](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_NormalsOpposed.md) | Read-only property that gets whether the directions of the normals are opposed or aligned. |
| [OccurrenceOne](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_OccurrenceOne.md) | Property that returns the first of the two objects this constraint is between. |
| [OccurrenceTwo](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_OccurrenceTwo.md) | Property that returns the second of the two objects this constraint is between. |
| [Parent](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_Parent.md) | Property that returns the parent of the object. |
| [ResultOfiMate](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ResultOfiMate.md) | Property that indicates if this iMateResult represents a composite iMate. |
| [ResultOfLayoutConstraint](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ResultOfLayoutConstraint.md) | Property that indicates if this constraint is a member of a layout constraint. If True then it is a member of a layout constraint. The layout constraint can be obtained by using the LayoutConstraint property. |
| [Suppressed](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_Suppressed.md) | Gets/Sets the Boolean flag indicating whether this constraint is suppressed. |
| [SymmetryPlane](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_SymmetryPlane.md) | Read-only property that returns the object that defines the symmetry plane. |
| [Type](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_Visible.md) | Gets/Sets the Visible indicating whether this constraint is visible. |

## Version

Introduced in version 2014
