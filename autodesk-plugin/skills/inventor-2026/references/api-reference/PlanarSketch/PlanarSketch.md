# PlanarSketch Object

Derived from: [Sketch](../Sketch/Sketch.md) Object

## Description

The PlanarSketch object, situated in 3D space. See the overview articles.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddArcSlotByCenterPointArc](../PlanarSketch/PlanarSketch_AddArcSlotByCenterPointArc.md) | Method that creates an arc slot. The sketch entities represent the sketch slot are returned. |
| [AddArcSlotByThreePointArc](../PlanarSketch/PlanarSketch_AddArcSlotByThreePointArc.md) | Method that creates an arc slot. The sketch entities represent the sketch slot are returned. |
| [AddByProjectingEntity](../PlanarSketch/PlanarSketch_AddByProjectingEntity.md) | Method that creates a new sketch entity by projecting other entities onto the sketch plane. This method performs the same function as the Project Geometry or Project DWG Geometry command according to the Entity you specified. |
| [AddBySilhouette](../PlanarSketch/PlanarSketch_AddBySilhouette.md) | Method that creates new reference sketch geometry as the silhouette on the input face near the input proximity point. |
| [AddStraightSlotByCenterToCenter](../PlanarSketch/PlanarSketch_AddStraightSlotByCenterToCenter.md) | Method that creates a straight slot. The sketch entities represent the sketch slot are returned. |
| [AddStraightSlotByOverall](../PlanarSketch/PlanarSketch_AddStraightSlotByOverall.md) | Method that creates a straight slot. The sketch entities represent the sketch slot are returned. |
| [AddStraightSlotBySlotCenter](../PlanarSketch/PlanarSketch_AddStraightSlotBySlotCenter.md) | Method that creates a straight slot. The sketch entities represent the sketch slot are returned. |
| [BreakLink](../PlanarSketch/PlanarSketch_BreakLink.md) | Method that breaks the link to the source sketch. |
| [CopyContentsTo](../PlanarSketch/PlanarSketch_CopyContentsTo.md) | Method that copies all the contents of the sketch to the \input target sketch. |
| [CopyEntitiesTo](../PlanarSketch/PlanarSketch_CopyEntitiesTo.md) | Method that copies sketch entities of the sketch to the input target sketch. |
| [Delete](../PlanarSketch/PlanarSketch_Delete.md) | Method that deletes the sketch. This method is only valid for sketches that are not used by a feature. |
| [Edit](../PlanarSketch/PlanarSketch_Edit.md) | Method that causes the Sketch environment to be invoked with this sketch available for interactive edit. |
| [ExitEdit](../PlanarSketch/PlanarSketch_ExitEdit.md) | Causes the Sketch environment to be closed and the user interface to return to the previous environment. This is equivalent to the Return command. This method is only valid in the case where this sketch is open for edit within the user interface. |
| [GetCustomLineType](../PlanarSketch/PlanarSketch_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetReferenceKey](../PlanarSketch/PlanarSketch_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [ModelToSketchSpace](../PlanarSketch/PlanarSketch_ModelToSketchSpace.md) | Method that takes a 3D coordinate in model space, projects it onto the sketch plane along the normal of the plane and returns a Point2d object containing the resulting coordinate point in sketch space. |
| [MoveSketchObjects](../PlanarSketch/PlanarSketch_MoveSketchObjects.md) | Method that moves a collection of sketch objects by a specified vector. If the Copy argument is set to True, the newly created objects are returned. |
| [OffsetSketchEntitiesUsingDistance](../PlanarSketch/PlanarSketch_OffsetSketchEntitiesUsingDistance.md) | Method that offsets a sketch entity or a group of connected sketch entities. In both cases, the base sketch entity is first offset by the specified distance and along the specified direction. The base sketch entity is determined as follows: \* If only one sketch entity needs to be offset, it will be treated as the base sketch entity. \* If a group of end-to-end connected entities need to be offset, the first entity in the group will be treated as the base sketch entity. If this method successfully offsets the specified input sketch entities, the newly created sketch entities are returned. |
| [OffsetSketchEntitiesUsingPoint](../PlanarSketch/PlanarSketch_OffsetSketchEntitiesUsingPoint.md) | Method that offsets a sketch entity or a group of end-to-end connected sketch entities. In both cases, the offset is first applied to the base sketch entity such that the offset of the base sketch entity passes through the specified offset point on the sketch. The shortest distance of this offset point from the original base sketch entity determines the offset distance. |
| [RotateSketchObjects](../PlanarSketch/PlanarSketch_RotateSketchObjects.md) | Method that rotates a collection of sketch objects by a specified angle. If the Copy argument is set to True, the newly created objects are returned. |
| [SetCustomLineType](../PlanarSketch/PlanarSketch_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |
| [SetEndOfPart](../PlanarSketch/PlanarSketch_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. The argument defines if the end-of-part marker will be positioned just before or just after the object. If the object is contained within another object and is not in the top level of the browser, the positioning of the marker will be relative to the top-level object the calling object is contained within. An example of this case is a sketch that has not been shared and has been consumed by a feature. Another example is a nested work feature. |
| [SketchToModelSpace](../PlanarSketch/PlanarSketch_SketchToModelSpace.md) | Method that takes a 2D coordinate in sketch space, and returns a Point3d containing the coordinates of the point in model space. |
| [Solve](../PlanarSketch/PlanarSketch_Solve.md) | Method that causes the sketch to solve. |
| [UpdateProfiles](../PlanarSketch/PlanarSketch_UpdateProfiles.md) | Method that updates all the profiles within the sketch. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../PlanarSketch/PlanarSketch_Adaptive.md) | Gets and sets whether the sketch is adaptive or not. |
| [Application](../PlanarSketch/PlanarSketch_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../PlanarSketch/PlanarSketch_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AxisEntity](../PlanarSketch/PlanarSketch_AxisEntity.md) | Gets and sets the object that defines the X or Y axis of the sketch plane. The AxisIsX property defines whether it is the X or Y axis, and the NaturalAxisDirection property defines the direction of the axis. |
| [AxisEntityGeometry](../PlanarSketch/PlanarSketch_AxisEntityGeometry.md) | Property that gets the geometry that describes the axis entity. |
| [AxisIsX](../PlanarSketch/PlanarSketch_AxisIsX.md) | Gets and sets if the axis entity defines the X or Y axis. True indicates the axis defines the X-axis. |
| [CheckSumValue](../PlanarSketch/PlanarSketch_CheckSumValue.md) | Gets sketch checksum value. |
| [CircularPatterns](../PlanarSketch/PlanarSketch_CircularPatterns.md) | Gets the SketchCircularPatterns collection object. |
| [Color](../PlanarSketch/PlanarSketch_Color.md) | Gets and Sets the color for the sketch. |
| [ConstraintStatus](../PlanarSketch/PlanarSketch_ConstraintStatus.md) | Property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [Consumed](../PlanarSketch/PlanarSketch_Consumed.md) | Gets whether the sketch is consumed or not. |
| [CopyToFlatPattern](../PlanarSketch/PlanarSketch_CopyToFlatPattern.md) | Gets and sets whether a sheet metal folded model sketch should be copied over (transposed) to the flat pattern. |
| [DataIO](../PlanarSketch/PlanarSketch_DataIO.md) | Gets the object through which this sketch's data content can be persisted. |
| [DeferUpdates](../PlanarSketch/PlanarSketch_DeferUpdates.md) | Gets and Sets whether to defer the solving of the sketch or not. |
| [Dependents](../PlanarSketch/PlanarSketch_Dependents.md) | Gets the dependent objects of the sketch. |
| [DimensionConstraints](../PlanarSketch/PlanarSketch_DimensionConstraints.md) | Gets the collection of all dimension constraints on the sketch. |
| [DimensionsVisible](../PlanarSketch/PlanarSketch_DimensionsVisible.md) | Gets and sets whether the dimensions on the sketch are visible. |
| [DisabledActionTypes](../PlanarSketch/PlanarSketch_DisabledActionTypes.md) | Gets and sets the action types valid for this sketch. |
| [Exported](../PlanarSketch/PlanarSketch_Exported.md) | Read-write property that gets and sets whether the object is exported. Objects must be marked for export in order for them to be derived. |
| [GeometricConstraints](../PlanarSketch/PlanarSketch_GeometricConstraints.md) | Property that returns the collection of all geometric constraints on the sketch. |
| [HasReferenceComponent](../PlanarSketch/PlanarSketch_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [HealthStatus](../PlanarSketch/PlanarSketch_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../PlanarSketch/PlanarSketch_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. This property should return True for sketches that are created as a result of an unfold or refold feature. |
| [LineType](../PlanarSketch/PlanarSketch_LineType.md) | Gets and Sets the line type override for the sketch. |
| [LineWeight](../PlanarSketch/PlanarSketch_LineWeight.md) | Gets and Sets the line weight override for the sketch. |
| [ModelToSketchTransform](../PlanarSketch/PlanarSketch_ModelToSketchTransform.md) | Property that returns the transformation from model space to the 2d sketch coordinate space. |
| [Name](../PlanarSketch/PlanarSketch_Name.md) | Gets and sets name of the sketch. |
| [NaturalAxisDirection](../PlanarSketch/PlanarSketch_NaturalAxisDirection.md) | Gets and sets if the sketch plane X or Y axis is in the same direction as that defined by axis entity. True indicates the axis direction is in the same direction as the axis. |
| [OriginPoint](../PlanarSketch/PlanarSketch_OriginPoint.md) | Gets and sets origin of the sketch. When set this property, the valid object can be a WorkPoint, Vertex or SketchPoint. |
| [OriginPointGeometry](../PlanarSketch/PlanarSketch_OriginPointGeometry.md) | Property that gets the geometry that describes the origin point. |
| [OwnedBy](../PlanarSketch/PlanarSketch_OwnedBy.md) | Property that returns the PartFeature object. This property should return the UnfoldFeature or RefoldFeature object that created the sketch. |
| [Parent](../PlanarSketch/PlanarSketch_Parent.md) | Property that gets the parent object from whom this object can logically be reached. |
| [PlanarEntity](../PlanarSketch/PlanarSketch_PlanarEntity.md) | Gets and sets the planar object that defines the planar object the sketch is to be built on. |
| [PlanarEntityGeometry](../PlanarSketch/PlanarSketch_PlanarEntityGeometry.md) | Property that returns the geometry that describes the plane the sketch is based on. |
| [Profiles](../PlanarSketch/PlanarSketch_Profiles.md) | Property that returns the Profiles collection object. |
| [ProjectedCuts](../PlanarSketch/PlanarSketch_ProjectedCuts.md) | Property that returns the ProjectedCuts collection object. This collection provides access to the existing projected cut edges in the sketch and provides functionality to create new projected cut edges. |
| [RectangularPatterns](../PlanarSketch/PlanarSketch_RectangularPatterns.md) | Gets the SketchRectangularPatterns collection object. |
| [ReferenceComponent](../PlanarSketch/PlanarSketch_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../PlanarSketch/PlanarSketch_ReferencedEntity.md) | Property that returns the referenced sketch in the cases where this sketch was created as a result of a "derive" operation or copied over to the sheet metal flat pattern from the folded model. |
| [Shared](../PlanarSketch/PlanarSketch_Shared.md) | Gets and sets whether the profile is shared or not. |
| [SketchArcs](../PlanarSketch/PlanarSketch_SketchArcs.md) | Property that returns the SketchArcs collection object. |
| [SketchBlocks](../PlanarSketch/PlanarSketch_SketchBlocks.md) | Property that returns the SketchBlocks collection object. Only the first level sketch blocks in the sketch are returned. Use SketchBlock.ChildBlocks property recursively to get sketch blocks at all levels. |
| [SketchCircles](../PlanarSketch/PlanarSketch_SketchCircles.md) | Property that returns the SketchArcs collection object. |
| [SketchControlPointSplines](../PlanarSketch/PlanarSketch_SketchControlPointSplines.md) | Read-only property that returns the SketchControlPointSplines collection object. This collection provides access to the existing control point splines in the sketch and provides functionality to create new control point splines. |
| [SketchEllipses](../PlanarSketch/PlanarSketch_SketchEllipses.md) | Property that returns the SketchEllipses collection object. |
| [SketchEllipticalArcs](../PlanarSketch/PlanarSketch_SketchEllipticalArcs.md) | Property that returns the SketchEllipticalArcs collection object. |
| [SketchEntities](../PlanarSketch/PlanarSketch_SketchEntities.md) | Property that returns the collection of all entities on the sketch, regardless of their type. |
| [SketchEquationCurves](../PlanarSketch/PlanarSketch_SketchEquationCurves.md) | Read-only property that returns the SketchEquationCurves collection object. This collection provides access to the existing equation curves in the sketch and provides functionality to create new equation curves. |
| [SketchFixedSplines](../PlanarSketch/PlanarSketch_SketchFixedSplines.md) | Property that gets the collection object. |
| [SketchImages](../PlanarSketch/PlanarSketch_SketchImages.md) | Property that returns a collection of all images on the sketch. |
| [SketchLines](../PlanarSketch/PlanarSketch_SketchLines.md) | Property that returns the SketchLines collection object. This collection provides access to the existing lines in the sketch and provides functionality to create new lines. |
| [SketchOffsetSplines](../PlanarSketch/PlanarSketch_SketchOffsetSplines.md) | Property that returns the collection object. This collection provides access to the existing offset splines in the sketch. |
| [SketchPoints](../PlanarSketch/PlanarSketch_SketchPoints.md) | Property that returns the SketchPoints collection object. |
| [SketchSplines](../PlanarSketch/PlanarSketch_SketchSplines.md) | Property that returns the SketchSplines collection object. |
| [SketchToModelTransform](../PlanarSketch/PlanarSketch_SketchToModelTransform.md) | Property that returns the transformation from the 2D sketch coordinate space to model space. |
| [TextBoxes](../PlanarSketch/PlanarSketch_TextBoxes.md) | Gets the TextBoxes collection associated with this Sketch. |
| [Type](../PlanarSketch/PlanarSketch_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../PlanarSketch/PlanarSketch_Visible.md) | Gets and sets the visibility of the sketch. |

## Accessed From

[HoleFeature.Sketch](../HoleFeature/HoleFeature_Sketch.md), [HoleFeatureProxy.Sketch](../HoleFeatureProxy/HoleFeatureProxy_Sketch.md), [PlanarSketch.ReferencedEntity](../PlanarSketch/PlanarSketch_ReferencedEntity.md), [PlanarSketches.Add](../PlanarSketches/PlanarSketches_Add.md), [PlanarSketches.AddWithOrientation](../PlanarSketches/PlanarSketches_AddWithOrientation.md), [PlanarSketches.Item](../PlanarSketches/PlanarSketches_Item.md), [PlanarSketchProxy.NativeObject](../PlanarSketchProxy/PlanarSketchProxy_NativeObject.md), [PlanarSketchProxy.ReferencedEntity](../PlanarSketchProxy/PlanarSketchProxy_ReferencedEntity.md), [ProjectedCut.Parent](../ProjectedCut/ProjectedCut_Parent.md), [ProjectedCutProxy.Parent](../ProjectedCutProxy/ProjectedCutProxy_Parent.md), [SketchBlockDefinition.ReferencedEntity](../SketchBlockDefinition/SketchBlockDefinition_ReferencedEntity.md), [SketchBlockDefinitionProxy.ReferencedEntity](../SketchBlockDefinitionProxy/SketchBlockDefinitionProxy_ReferencedEntity.md)

## Derived Classes

[PlanarSketchProxy](../PlanarSketchProxy/PlanarSketchProxy.md), [SketchBlockDefinition](../SketchBlockDefinition/SketchBlockDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Copy a sketch](../../sample-programs/CopySketch_Sample.md) | This sample demonstrates copying the contents of a sketch into another sketch via the API. |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |
| [Using Inventor's error dialog](../../sample-programs/ErrorManager_Sample.md) | Demonstrates using Inventor's error dialog. |
| [Edit profile of an extrude feature](../../sample-programs/ExtrudeFeature_Profile_Sample.md) | This sample demonstrates editing the profile of an extrude feature. |
| [Create sheet metal face and fold features](../../sample-programs/FoldFeatures_Add_Sample.md) | This sample demonstrates the creation of sheet metal face and fold features. |
| [Create and Edit an Extrude Feature with a pocket](../../sample-programs/PartFeature_SetEndOfPart_Sample.md) | This sample demonstrates how to edit an extrude feature. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Sketch from Face Silhouette](../../sample-programs/PlanarSketch_AddBySilhouette_Sample.md) | This sample creates a cylindrical solid, creates a new sketch plane and creates some new sketch lines from the actual edges and the apparent (silhouette) edges of the cylinder. |
| [Sketch Edit Orientation](../../sample-programs/PlanarSketch_NaturalAxisDirection_Sample.md) | This sample demonstrates modifying the orientation of a sketch. |
| [Sketch Share](../../sample-programs/PlanarSketch_Shared_Sample.md) | This sample demonstrates setting a sketch so it is shared. |
| [Sketch Add](../../sample-programs/PlanarSketches_Add_Sample.md) | This sample demonstrates the creation of a sketch using the Sketches.Add method. |
| [Sketch Add Oriented](../../sample-programs/PlanarSketches_AddWithOrientation_Sample.md) | This sample demonstrates the creation of a sketch using the Sketches.AddWithOrientation method. |
| [Querying a sketch profile to get regions.](../../sample-programs/Profile_RegionProperties_Sample.md) | This sample demonstrates getting region properties from a sketch profile. |
| [Sketch profile control](../../sample-programs/ProfilePath_AddsMaterial_Sample.md) | This sample demonstrates the usage of the Profiles API to control the shape of the profile. The sample creates three concntric circles and creates an extrusion of the region between the inner circles. |
| [Add a punch tool feature](../../sample-programs/PunchToolFeatures_Add_Sample.md) | This program demonstrates the creation of a punch tool feature. It uses one of the punch features that's delivered with Inventor. It assumes you already have an existing sheet metal part and have selected a face to place the punch feature on. The selected face should be large so there is room for the punch features. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |
| [Projection - project across parts](../../sample-programs/Sketch_AddByProjectingEntity_Sample.md) | This sample demonstrates projecting a sketch entity across parts in an assembly. To use the sample, have an assembly open that contains at least two occurrences, (parts only), and run the program. |
| [Sketch Delete](../../sample-programs/Sketch_Delete_Sample.md) | This sample demonstrates deleting a sketch. |
| [Sketch Open for Edit](../../sample-programs/Sketch_Edit_Sample.md) | This sample demonstrates opening a sketch for edit. |
| [Offset a 2D sketch](../../sample-programs/Sketch_OffsetSketchEntitiesUsingDistance_Sample.md) | This sample demonstrates the creation of offsets in 2d sketches. Two ways of creating the offset are shown - one uses a distance and the other uses the input point. |
| [Sketch Lines](../../sample-programs/Sketch_SketchLines_Sample.md) | This sample demonstrates creating lines. It uses all of the various methods to create lines, both singly and as rectangles. |
| [Set Sketch Visibility](../../sample-programs/Sketch_Visible_Sample.md) | This sample demonstrates setting the visibility of a sketch. |
| [Create and insert a sketch block definition into a part sketch](../../sample-programs/SketchBlockDefinition_Sample.md) | This sample demonstrates inserting a sketch block into a part sketch. |
| [Create sketch block from an existing sketch](../../sample-programs/SketchBlocks_Add_Sample.md) | This sample demonstrates creating a sketch block from an existing sketch. |
| [Create sketch elliptical arc](../../sample-programs/SketchEllipticalArc_Sample.md) | This sample demonstrates creating an elliptical arc in a sketch and dimensioning its minor radius. |
| [Spline - create NURBS](../../sample-programs/SketchFixedSpline_Sample.md) | This sample demonstrates the creation of a sketch spline using a geometry definition (a NURB). The API also supports creation of 3D sketch splines in a similar way. |
| [Sketch Spline](../../sample-programs/SketchSpline_Sample.md) | This sample demonstrates creating and manipulating a sketch spline. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |

## Version

Introduced in version 5
