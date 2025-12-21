# PlanarSketchProxy Object

Derived from: [PlanarSketch](../PlanarSketch/PlanarSketch.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddArcSlotByCenterPointArc](../PlanarSketchProxy/PlanarSketchProxy_AddArcSlotByCenterPointArc.md) | Method that creates an arc slot. The sketch entities represent the sketch slot are returned. |
| [AddArcSlotByThreePointArc](../PlanarSketchProxy/PlanarSketchProxy_AddArcSlotByThreePointArc.md) | Method that creates an arc slot. The sketch entities represent the sketch slot are returned. |
| [AddByProjectingEntity](../PlanarSketchProxy/PlanarSketchProxy_AddByProjectingEntity.md) | Method that creates a new sketch entity by projecting other entities onto the sketch plane. This method performs the same function as the Project Geometry or Project DWG Geometry command according to the Entity you specified. |
| [AddBySilhouette](../PlanarSketchProxy/PlanarSketchProxy_AddBySilhouette.md) | Method that creates new reference sketch geometry as the silhouette on the input face near the input proximity point. |
| [AddStraightSlotByCenterToCenter](../PlanarSketchProxy/PlanarSketchProxy_AddStraightSlotByCenterToCenter.md) | Method that creates a straight slot. The sketch entities represent the sketch slot are returned. |
| [AddStraightSlotByOverall](../PlanarSketchProxy/PlanarSketchProxy_AddStraightSlotByOverall.md) | Method that creates a straight slot. The sketch entities represent the sketch slot are returned. |
| [AddStraightSlotBySlotCenter](../PlanarSketchProxy/PlanarSketchProxy_AddStraightSlotBySlotCenter.md) | Method that creates a straight slot. The sketch entities represent the sketch slot are returned. |
| [BreakLink](../PlanarSketchProxy/PlanarSketchProxy_BreakLink.md) | Method that breaks the link to the source sketch. |
| [CopyContentsTo](../PlanarSketchProxy/PlanarSketchProxy_CopyContentsTo.md) | Method that copies all the contents of the sketch to the \input target sketch. |
| [CopyEntitiesTo](../PlanarSketchProxy/PlanarSketchProxy_CopyEntitiesTo.md) | Method that copies sketch entities of the sketch to the input target sketch. |
| [Delete](../PlanarSketchProxy/PlanarSketchProxy_Delete.md) | Method that deletes the sketch. This method is only valid for sketches that are not used by a feature. |
| [Edit](../PlanarSketchProxy/PlanarSketchProxy_Edit.md) | Method that causes the Sketch environment to be invoked with this sketch available for interactive edit. |
| [ExitEdit](../PlanarSketchProxy/PlanarSketchProxy_ExitEdit.md) | Causes the Sketch environment to be closed and the user interface to return to the previous environment. This is equivalent to the Return command. This method is only valid in the case where this sketch is open for edit within the user interface. |
| [GetCustomLineType](../PlanarSketchProxy/PlanarSketchProxy_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetReferenceKey](../PlanarSketchProxy/PlanarSketchProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [ModelToSketchSpace](../PlanarSketchProxy/PlanarSketchProxy_ModelToSketchSpace.md) | Method that takes a 3D coordinate in model space, projects it onto the sketch plane along the normal of the plane and returns a Point2d object containing the resulting coordinate point in sketch space. |
| [MoveSketchObjects](../PlanarSketchProxy/PlanarSketchProxy_MoveSketchObjects.md) | Method that moves a collection of sketch objects by a specified vector. If the Copy argument is set to True, the newly created objects are returned. |
| [OffsetSketchEntitiesUsingDistance](../PlanarSketchProxy/PlanarSketchProxy_OffsetSketchEntitiesUsingDistance.md) | Method that offsets a sketch entity or a group of connected sketch entities. In both cases, the base sketch entity is first offset by the specified distance and along the specified direction. The base sketch entity is determined as follows: \* If only one sketch entity needs to be offset, it will be treated as the base sketch entity. \* If a group of end-to-end connected entities need to be offset, the first entity in the group will be treated as the base sketch entity. If this method successfully offsets the specified input sketch entities, the newly created sketch entities are returned. |
| [OffsetSketchEntitiesUsingPoint](../PlanarSketchProxy/PlanarSketchProxy_OffsetSketchEntitiesUsingPoint.md) | Method that offsets a sketch entity or a group of end-to-end connected sketch entities. In both cases, the offset is first applied to the base sketch entity such that the offset of the base sketch entity passes through the specified offset point on the sketch. The shortest distance of this offset point from the original base sketch entity determines the offset distance. |
| [RotateSketchObjects](../PlanarSketchProxy/PlanarSketchProxy_RotateSketchObjects.md) | Method that rotates a collection of sketch objects by a specified angle. If the Copy argument is set to True, the newly created objects are returned. |
| [SetCustomLineType](../PlanarSketchProxy/PlanarSketchProxy_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |
| [SetEndOfPart](../PlanarSketchProxy/PlanarSketchProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. The argument defines if the end-of-part marker will be positioned just before or just after the object. If the object is contained within another object and is not in the top level of the browser, the positioning of the marker will be relative to the top-level object the calling object is contained within. An example of this case is a sketch that has not been shared and has been consumed by a feature. Another example is a nested work feature. |
| [SketchToModelSpace](../PlanarSketchProxy/PlanarSketchProxy_SketchToModelSpace.md) | Method that takes a 2D coordinate in sketch space, and returns a Point3d containing the coordinates of the point in model space. |
| [Solve](../PlanarSketchProxy/PlanarSketchProxy_Solve.md) | Method that causes the sketch to solve. |
| [UpdateProfiles](../PlanarSketchProxy/PlanarSketchProxy_UpdateProfiles.md) | Method that updates all the profiles within the sketch. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../PlanarSketchProxy/PlanarSketchProxy_Adaptive.md) | Gets and sets whether the sketch is adaptive or not. |
| [Application](../PlanarSketchProxy/PlanarSketchProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../PlanarSketchProxy/PlanarSketchProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AxisEntity](../PlanarSketchProxy/PlanarSketchProxy_AxisEntity.md) | Gets and sets the object that defines the X or Y axis of the sketch plane. The AxisIsX property defines whether it is the X or Y axis, and the NaturalAxisDirection property defines the direction of the axis. |
| [AxisEntityGeometry](../PlanarSketchProxy/PlanarSketchProxy_AxisEntityGeometry.md) | Property that gets the geometry that describes the axis entity. |
| [AxisIsX](../PlanarSketchProxy/PlanarSketchProxy_AxisIsX.md) | Gets and sets if the axis entity defines the X or Y axis. True indicates the axis defines the X-axis. |
| [CheckSumValue](../PlanarSketchProxy/PlanarSketchProxy_CheckSumValue.md) | Gets sketch checksum value. |
| [CircularPatterns](../PlanarSketchProxy/PlanarSketchProxy_CircularPatterns.md) | Gets the SketchCircularPatterns collection object. |
| [Color](../PlanarSketchProxy/PlanarSketchProxy_Color.md) | Gets and Sets the color for the sketch. |
| [ConstraintStatus](../PlanarSketchProxy/PlanarSketchProxy_ConstraintStatus.md) | Property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [Consumed](../PlanarSketchProxy/PlanarSketchProxy_Consumed.md) | Gets whether the sketch is consumed or not. |
| [ContainingOccurrence](../PlanarSketchProxy/PlanarSketchProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [CopyToFlatPattern](../PlanarSketchProxy/PlanarSketchProxy_CopyToFlatPattern.md) | Gets and sets whether a sheet metal folded model sketch should be copied over (transposed) to the flat pattern. |
| [DataIO](../PlanarSketchProxy/PlanarSketchProxy_DataIO.md) | Gets the object through which this sketch's data content can be persisted. |
| [DeferUpdates](../PlanarSketchProxy/PlanarSketchProxy_DeferUpdates.md) | Gets and Sets whether to defer the solving of the sketch or not. |
| [Dependents](../PlanarSketchProxy/PlanarSketchProxy_Dependents.md) | Gets the dependent objects of the sketch. |
| [DimensionConstraints](../PlanarSketchProxy/PlanarSketchProxy_DimensionConstraints.md) | Gets the collection of all dimension constraints on the sketch. |
| [DimensionsVisible](../PlanarSketchProxy/PlanarSketchProxy_DimensionsVisible.md) | Gets and sets whether the dimensions on the sketch are visible. |
| [DisabledActionTypes](../PlanarSketchProxy/PlanarSketchProxy_DisabledActionTypes.md) | Gets and sets the action types valid for this sketch. |
| [Exported](../PlanarSketchProxy/PlanarSketchProxy_Exported.md) | Read-write property that gets and sets whether the object is exported. Objects must be marked for export in order for them to be derived. |
| [GeometricConstraints](../PlanarSketchProxy/PlanarSketchProxy_GeometricConstraints.md) | Property that returns the collection of all geometric constraints on the sketch. |
| [HasReferenceComponent](../PlanarSketchProxy/PlanarSketchProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [HealthStatus](../PlanarSketchProxy/PlanarSketchProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../PlanarSketchProxy/PlanarSketchProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. This property should return True for sketches that are created as a result of an unfold or refold feature. |
| [LineType](../PlanarSketchProxy/PlanarSketchProxy_LineType.md) | Gets and Sets the line type override for the sketch. |
| [LineWeight](../PlanarSketchProxy/PlanarSketchProxy_LineWeight.md) | Gets and Sets the line weight override for the sketch. |
| [ModelToSketchTransform](../PlanarSketchProxy/PlanarSketchProxy_ModelToSketchTransform.md) | Property that returns the transformation from model space to the 2d sketch coordinate space. |
| [Name](../PlanarSketchProxy/PlanarSketchProxy_Name.md) | Gets and sets name of the sketch. |
| [NativeObject](../PlanarSketchProxy/PlanarSketchProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [NaturalAxisDirection](../PlanarSketchProxy/PlanarSketchProxy_NaturalAxisDirection.md) | Gets and sets if the sketch plane X or Y axis is in the same direction as that defined by axis entity. True indicates the axis direction is in the same direction as the axis. |
| [OriginPoint](../PlanarSketchProxy/PlanarSketchProxy_OriginPoint.md) | Gets and sets origin of the sketch. When set this property, the valid object can be a WorkPoint, Vertex or SketchPoint. |
| [OriginPointGeometry](../PlanarSketchProxy/PlanarSketchProxy_OriginPointGeometry.md) | Property that gets the geometry that describes the origin point. |
| [OwnedBy](../PlanarSketchProxy/PlanarSketchProxy_OwnedBy.md) | Property that returns the PartFeature object. This property should return the UnfoldFeature or RefoldFeature object that created the sketch. |
| [Parent](../PlanarSketchProxy/PlanarSketchProxy_Parent.md) | Property that gets the parent object from whom this object can logically be reached. |
| [PlanarEntity](../PlanarSketchProxy/PlanarSketchProxy_PlanarEntity.md) | Gets and sets the planar object that defines the planar object the sketch is to be built on. |
| [PlanarEntityGeometry](../PlanarSketchProxy/PlanarSketchProxy_PlanarEntityGeometry.md) | Property that returns the geometry that describes the plane the sketch is based on. |
| [Profiles](../PlanarSketchProxy/PlanarSketchProxy_Profiles.md) | Property that returns the Profiles collection object. |
| [ProjectedCuts](../PlanarSketchProxy/PlanarSketchProxy_ProjectedCuts.md) | Property that returns the ProjectedCuts collection object. This collection provides access to the existing projected cut edges in the sketch and provides functionality to create new projected cut edges. |
| [RectangularPatterns](../PlanarSketchProxy/PlanarSketchProxy_RectangularPatterns.md) | Gets the SketchRectangularPatterns collection object. |
| [ReferenceComponent](../PlanarSketchProxy/PlanarSketchProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../PlanarSketchProxy/PlanarSketchProxy_ReferencedEntity.md) | Property that returns the referenced sketch in the cases where this sketch was created as a result of a "derive" operation or copied over to the sheet metal flat pattern from the folded model. |
| [Shared](../PlanarSketchProxy/PlanarSketchProxy_Shared.md) | Gets and sets whether the profile is shared or not. |
| [SketchArcs](../PlanarSketchProxy/PlanarSketchProxy_SketchArcs.md) | Property that returns the SketchArcs collection object. |
| [SketchBlocks](../PlanarSketchProxy/PlanarSketchProxy_SketchBlocks.md) | Property that returns the SketchBlocks collection object. Only the first level sketch blocks in the sketch are returned. Use SketchBlock.ChildBlocks property recursively to get sketch blocks at all levels. |
| [SketchCircles](../PlanarSketchProxy/PlanarSketchProxy_SketchCircles.md) | Property that returns the SketchArcs collection object. |
| [SketchControlPointSplines](../PlanarSketchProxy/PlanarSketchProxy_SketchControlPointSplines.md) | Read-only property that returns the SketchControlPointSplines collection object. This collection provides access to the existing control point splines in the sketch and provides functionality to create new control point splines. |
| [SketchEllipses](../PlanarSketchProxy/PlanarSketchProxy_SketchEllipses.md) | Property that returns the SketchEllipses collection object. |
| [SketchEllipticalArcs](../PlanarSketchProxy/PlanarSketchProxy_SketchEllipticalArcs.md) | Property that returns the SketchEllipticalArcs collection object. |
| [SketchEntities](../PlanarSketchProxy/PlanarSketchProxy_SketchEntities.md) | Property that returns the collection of all entities on the sketch, regardless of their type. |
| [SketchEquationCurves](../PlanarSketchProxy/PlanarSketchProxy_SketchEquationCurves.md) | Read-only property that returns the SketchEquationCurves collection object. This collection provides access to the existing equation curves in the sketch and provides functionality to create new equation curves. |
| [SketchFixedSplines](../PlanarSketchProxy/PlanarSketchProxy_SketchFixedSplines.md) | Property that gets the collection object. |
| [SketchImages](../PlanarSketchProxy/PlanarSketchProxy_SketchImages.md) | Property that returns a collection of all images on the sketch. |
| [SketchLines](../PlanarSketchProxy/PlanarSketchProxy_SketchLines.md) | Property that returns the SketchLines collection object. This collection provides access to the existing lines in the sketch and provides functionality to create new lines. |
| [SketchOffsetSplines](../PlanarSketchProxy/PlanarSketchProxy_SketchOffsetSplines.md) | Property that returns the collection object. This collection provides access to the existing offset splines in the sketch. |
| [SketchPoints](../PlanarSketchProxy/PlanarSketchProxy_SketchPoints.md) | Property that returns the SketchPoints collection object. |
| [SketchSplines](../PlanarSketchProxy/PlanarSketchProxy_SketchSplines.md) | Property that returns the SketchSplines collection object. |
| [SketchToModelTransform](../PlanarSketchProxy/PlanarSketchProxy_SketchToModelTransform.md) | Property that returns the transformation from the 2D sketch coordinate space to model space. |
| [TextBoxes](../PlanarSketchProxy/PlanarSketchProxy_TextBoxes.md) | Gets the TextBoxes collection associated with this Sketch. |
| [Type](../PlanarSketchProxy/PlanarSketchProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../PlanarSketchProxy/PlanarSketchProxy_Visible.md) | Gets and sets the visibility of the sketch. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |