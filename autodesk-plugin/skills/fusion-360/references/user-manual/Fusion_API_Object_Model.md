# AUTODESK® Fusion 360 API Object Model

> **Date:** September 21, 2017

## Legend

| Symbol | Description |
|--------|-------------|
| `[X]` | Base Class Objects |
| `(X)` | Derived Objects |
| Standard box | Collection Objects |
| Standard box | Standard Objects |

### Object Categories (Color-coded in original diagram)

- **Modeling Related Objects**
- **Assembly Related Objects**
- **User Interface Related Objects**
- **Construction Geometry Objects**
- **Body Related Objects**
- **Sketch Related Objects**

---

## Application

### Core Application Objects

- **Application**
  - `Documents`
  - `Document [O]`
    - `FusionDocument` (O)
  - `Data`
    - `DataHubs`
      - `DataHub`
    - `DataProjects`
      - `DataProject`
        - `DataFolders`
          - `DataFolder`
            - `DataFiles`
              - `DataFile`
  - `Products`
    - `Product [A]`
      - `Design` (A)
      - `CAM` (A)

### Preferences

- `Preferences`
  - `GeneralPreferences`
  - `MaterialPreferences`
  - `GraphicsPreferences`
  - `NetworkPreferences`
  - `UnitAndValuePreferences`
  - `GridPreferences`
  - `ProductPreferencesCollection`
    - `ProductPreferences [N]`
      - `FusionProductPreferences` (N)
  - `DefaultUnitsPreferencesCollection`
    - `DefaultUnitsPreferences [M]`
      - `FusionDefaultUnitsPreferences` (M)

---

## Design Structure

### Component Hierarchy

```
Design (A)
├── Component (Root)
│   ├── Occurrences
│   │   ├── Occurrence
│   │   │   └── OccurrenceList
│   │   └── Component (referenced)
│   └── Components
```

### BRep (Boundary Representation) Bodies

```
Component
└── BRepBodies
    └── BRepBody
        ├── BRepLumps
        │   └── BRepLump
        │       └── BRepShells
        │           └── BRepShell
        │               └── BRepFaces
        │                   └── BRepFace
        │                       ├── BRepLoops
        │                       │   └── BRepLoop
        │                       │       └── BRepCoEdges
        │                       │           └── BRepCoEdge
        │                       └── SurfaceEvaluator
        ├── BRepEdges
        │   └── BRepEdge
        │       └── CurveEvaluator3D
        ├── BRepVertices
        │   └── BRepVertex
        └── BRepCells
            └── BRepCell
```

### Mesh Bodies

```
Component
└── MeshBodies
    └── MeshBody
        └── MeshManager
            ├── TriangleMeshCalculator
            ├── TriangleMeshList
            │   └── TriangleMesh
            └── PolygonMesh
```

---

## Features

### Feature Base Class

```
Features
└── Feature [K]
```

### Primitive Features

| Feature Type | Input Class | Feature Class |
|--------------|-------------|---------------|
| Box | - | `BoxFeature` (K) |
| Cylinder | - | `CylinderFeature` (K) |
| Sphere | - | `SphereFeature` (K) |
| Torus | - | `TorusFeature` (K) |
| Pipe | - | `PipeFeature` (K) |
| Coil | - | `CoilFeature` (K) |

### Extrude Features

```
ExtrudeFeatures
└── ExtrudeFeature (K)
    └── ExtrudeFeatureInput
```

### Revolve Features

```
RevolveFeatures
└── RevolveFeature (K)
    └── RevolveFeatureInput
```

### Sweep Features

```
SweepFeatures
└── SweepFeature (K)
    └── SweepFeatureInput
```

### Loft Features

```
LoftFeatures
└── LoftFeature (K)
    └── LoftFeatureInput
        ├── LoftSections
        │   └── LoftSection
        ├── LoftCenterLineOrRails
        │   └── LoftCenterLineOrRail
        └── LoftEndCondition [EE]
            ├── LoftDirectionEndCondition (EE)
            ├── LoftFreeEndCondition (EE)
            ├── LoftPointSharpEndCondition (EE)
            ├── LoftPointTangentEndCondition (EE)
            ├── LoftSmoothEndCondition (EE)
            └── LoftTangentEndCondition (EE)
```

### Hole Features

```
HoleFeatures
└── HoleFeature (K)
    └── HoleFeatureInput
        └── HolePositionDefinition [DD]
            ├── AtCenterHolePositionDefinition (DD)
            ├── OnEdgeHolePositionDefinition (DD)
            ├── PlaneAndOffsetsHolePositionDefinition (DD)
            ├── PointHolePositionDefinition (DD)
            └── SketchPointsHolePositionDefinition (DD)
```

### Thread Features

```
ThreadFeatures
└── ThreadFeature (K)
    └── ThreadFeatureInput
        └── ThreadInfo
            └── ThreadDataQuery
```

### Pattern Features

| Pattern Type | Input Class | Feature Class |
|--------------|-------------|---------------|
| Circular Pattern | `CircularPatternFeatureInput` | `CircularPatternFeature` (K) |
| Rectangular Pattern | `RectangularPatternFeatureInput` | `RectangularPatternFeature` (K) |
| Mirror | `MirrorFeatureInput` | `MirrorFeature` (K) |
| Path Pattern | `PathPatternFeatureInput` | `PathPatternFeature` (K) |

Each pattern feature has:
```
PatternElements
└── PatternElement
```

### Fillet Features

```
FilletFeatures
└── FilletFeature (K)
    └── FilletFeatureInput
        └── FilletEdgeSets
            └── FilletEdgeSet [Y]
                ├── ConstantRadiusFilletEdgeSet (Y)
                ├── ChordLengthFilletEdgeSet (Y)
                └── VariableRadiusFilletEdgeSet (Y)
```

### Chamfer Features

```
ChamferFeatures
└── ChamferFeature (K)
    └── ChamferFeatureInput
        └── ChamferTypeDefinition [X]
            ├── DistanceAndAngleChamferTypeDefinition (X)
            ├── EqualDistanceChamferTypeDefinition (X)
            └── TwoDistancesChamferTypeDefinition (X)
```

### Shell Features

```
ShellFeatures
└── ShellFeature (K)
    └── ShellFeatureInput
```

### Draft Features

```
DraftFeatures
└── DraftFeature (K)
    └── DraftFeatureInput
```

### Split Features

| Feature Type | Input Class | Feature Class |
|--------------|-------------|---------------|
| Split Body | `SplitBodyFeatureInput` | `SplitBodyFeature` (K) |
| Split Face | `SplitFaceFeatureInput` | `SplitFaceFeature` (K) |
| Silhouette Split | `SilhouetteSplitFeatureInput` | `SilhouetteSplitFeature` (K) |

### Surface Features

| Feature Type | Input Class | Feature Class |
|--------------|-------------|---------------|
| Patch | `PatchFeatureInput` | `PatchFeature` (K) |
| Stitch | `StitchFeatureInput` | `StitchFeature` (K) |
| Unstitch | - | `UnstitchFeature` (K) |
| Thicken | `ThickenFeatureInput` | `ThickenFeature` (K) |
| Offset | `OffsetFeatureInput` | `OffsetFeature` (K) |
| Offset Faces | - | `OffsetFacesFeature` (K) |
| Boundary Fill | `BoundaryFillFeatureInput` | `BoundaryFillFeature` (K) |
| Trim | `TrimFeatureInput` | `TrimFeature` (K) |
| Extend | `ExtendFeatureInput` | `ExtendFeature` (K) |
| Reverse Normal | - | `ReverseNormalFeature` (K) |
| Delete Face | - | `DeleteFaceFeature` (K) |
| Surface Delete Face | - | `SurfaceDeleteFaceFeature` (K) |
| Replace Face | `ReplaceFaceFeatureInput` | `ReplaceFaceFeature` (K) |

### Other Features

| Feature Type | Input Class | Feature Class |
|--------------|-------------|---------------|
| Move | `MoveFeatureInput` | `MoveFeature` (K) |
| Scale | `ScaleFeatureInput` | `ScaleFeature` (K) |
| Rib | - | `RibFeature` (K) |
| Web | - | `WebFeature` (K) |
| Rule Fillet | - | `RuleFilletFeature` (K) |
| Base | - | `BaseFeature` (K) |
| Form | - | `FormFeature` (K) |
| Remove | - | `RemoveFeature` (K) |

### Copy/Cut Paste Bodies

```
CopyPasteBodies
└── CopyPasteBody

CutPasteBodies
└── CutPasteBody
```

---

## Extent Definitions

```
ExtentDefinition [L]
├── DistanceExtentDefinition (L)
├── AngleExtentDefinition (L)
├── TwoSideAngleExtentDefinition (L)
├── OneSideToExtentDefinition (L)
├── TwoSideToExtentDefinition (L)
├── AllExtentDefinition (L)
├── SymmetricExtentDefinition (L)
├── ThroughAllExtentDefinition (L)
├── ToEntityExtentDefinition (L)
├── FromEntityStartDefinition (L)
├── OffsetStartDefinition (L)
├── ProfilePlaneStartDefinition (L)
└── SketchPointHolePositionDefinition (L)
```

---

## Sketches

### Sketch Structure

```
Component
└── Sketches
    └── Sketch
        ├── SketchCurves
        │   └── SketchCurve [R] (Q)
        ├── SketchPoints
        │   └── SketchPoint (Q)
        ├── Profiles
        │   └── Profile
        │       └── ProfileLoops
        │           └── ProfileLoop
        │               └── ProfileCurves
        │                   └── ProfileCurve
        ├── SketchDimensions
        │   └── SketchDimension [T]
        ├── GeometricConstraints
        │   └── GeometricConstraint [S]
        └── SketchTexts
            └── SketchText (Q)
                └── SketchTextInput
```

### Sketch Entity Base Class

```
SketchEntity [Q]
├── SketchPoint (Q)
├── SketchCurve [R] (Q)
└── SketchText (Q)
```

### Sketch Curves

```
SketchCurve [R]
├── SketchLines
│   └── SketchLine (R)
├── SketchArcs
│   └── SketchArc (R)
├── SketchCircles
│   └── SketchCircle (R)
├── SketchEllipses
│   └── SketchEllipse (R)
├── SketchEllipticalArcs
│   └── SketchEllipticalArc (R)
├── SketchFittedSplines
│   └── SketchFittedSpline (R)
├── SketchFixedSplines
│   └── SketchFixedSpline (R)
└── SketchConicCurves
    └── SketchConicCurve (R)
```

### Sketch Dimensions

```
SketchDimension [T]
├── SketchLinearDimension (T)
├── SketchAngularDimension (T)
├── SketchDiameterDimension (T)
├── SketchRadialDimension (T)
├── SketchEllipseMajorRadiusDimension (T)
├── SketchEllipseMinorRadiusDimension (T)
├── SketchConcentricCircleDimension (T)
├── SketchOffsetCurvesDimension (T)
└── SketchOffsetDimension (T)
```

### Geometric Constraints

```
GeometricConstraint [S]
├── CoincidentConstraint (S)
├── CollinearConstraint (S)
├── ConcentricConstraint (S)
├── MidPointConstraint (S)
├── ParallelConstraint (S)
├── PerpendicularConstraint (S)
├── HorizontalConstraint (S)
├── HorizontalPointsConstraint (S)
├── VerticalConstraint (S)
├── VerticalPointsConstraint (S)
├── TangentConstraint (S)
├── SmoothConstraint (S)
├── EqualConstraint (S)
├── SymmetryConstraint (S)
├── CircularPatternConstraint (S)
├── RectangularPatternConstraint (S)
└── PolygonConstraint (S)
```

---

## Construction Geometry

### Construction Planes

```
ConstructionPlanes
└── ConstructionPlane
    └── ConstructionPlaneInput
        └── ConstructionPlaneDefinition [D]
            ├── ConstructionPlaneOffsetDefinition (D)
            ├── ConstructionPlaneAtAngleDefinition (D)
            ├── ConstructionPlaneByPlaneDefinition (D)
            ├── ConstructionPlaneTangentDefinition (D)
            ├── ConstructionPlaneMidplaneDefinition (D)
            ├── ConstructionPlaneTwoEdgesDefinition (D)
            ├── ConstructionPlaneThreePointsDefinition (D)
            ├── ConstructionPlaneTangentAtPointDefinition (D)
            └── ConstructionPlaneDistanceOnPathDefinition (D)
```

### Construction Axes

```
ConstructionAxes
└── ConstructionAxis
    └── ConstructionAxisInput
        └── ConstructionAxisDefinition [E]
            ├── ConstructionAxisByLineDefinition (E)
            ├── ConstructionAxisCircularFaceDefinition (E)
            ├── ConstructionAxisPerpendicularAtPointDefinition (E)
            ├── ConstructionAxisTwoPlaneDefinition (E)
            ├── ConstructionAxisTwoPointDefinition (E)
            ├── ConstructionAxisEdgeDefinition (E)
            └── ConstructionAxisNormalToFaceAtPointDefinition (E)
```

### Construction Points

```
ConstructionPoints
└── ConstructionPoint
    └── ConstructionPointInput
        └── ConstructionPointDefinition [F]
            ├── ConstructionPointPointDefinition (F)
            ├── ConstructionPointTwoEdgesDefinition (F)
            ├── ConstructionPointThreePlanesDefinition (F)
            ├── ConstructionPointEdgePlaneDefinition (F)
            └── ConstructionPointCenterDefinition (F)
```

---

## Joints and Assembly

### Joints

```
Joints
└── Joint
    └── JointInput
        ├── JointGeometry
        └── JointMotion [BB]
            ├── BallJointMotion (BB)
            ├── CylindricalJointMotion (BB)
            ├── PinSlotJointMotion (BB)
            ├── PlanarJointMotion (BB)
            ├── RevoluteJointMotion (BB)
            ├── RigidJointMotion (BB)
            └── SliderJointMotion (BB)
```

Each motion type (except Rigid) has:
```
JointLimits
```

### Joint Origins

```
JointOrigins
└── JointOrigin
    └── JointOriginInput
```

### As-Built Joints

```
AsBuiltJoints
└── AsBuiltJoint
    └── AsBuiltJointInput
```

### Rigid Groups

```
RigidGroups
└── RigidGroup
```

### Contact Sets

```
ContactSets
└── ContactSet
```

### Interference

```
InterferenceInput
└── InterferenceResults
    └── InterferenceResult
```

---

## Parameters

```
UserParameters
└── UserParameter (P)

ModelParameters
└── ModelParameter (P)

ParameterList
└── Parameter [P]
```

---

## Timeline

```
Timeline
├── TimelineGroups
│   └── TimelineGroup
├── TimelineObject
└── Snapshots
    └── Snapshot
```

---

## Materials and Appearances

### Material Libraries

```
MaterialLibraries
└── MaterialLibrary
    ├── Materials
    │   └── Material
    │       └── Properties
    │           └── Property [CC]
    └── Appearances
        └── Appearance
            └── Properties
                └── Property [CC]
```

### Favorite Materials/Appearances

```
FavoriteMaterials
FavoriteAppearances
```

### Appearance Textures

```
AppearanceTexture
└── AppearanceTextureProperty (CC)
```

### Property Types

```
Property [CC]
├── ColorProperty (CC)
├── FilenameProperty (CC)
├── FloatProperty (CC)
├── IntegerProperty (CC)
├── StringProperty (CC)
├── ChoiceProperty (CC)
├── BooleanProperty (CC)
└── AppearanceTextureProperty (CC)
```

---

## User Interface

### UserInterface Structure

```
Application
└── UserInterface
    ├── Workspaces
    │   └── Workspace
    ├── Toolbars
    │   └── Toolbar
    │       └── ToolbarControls
    │           └── ToolbarControl [V]
    ├── ToolbarPanels
    │   └── ToolbarPanel
    │       └── ToolbarPanelList
    ├── CommandDefinitions
    │   └── CommandDefinition
    │       └── ControlDefinition [U]
    ├── Palettes
    │   └── Palette [FF]
    │       └── TextCommandPalette (FF)
    ├── Selections
    ├── FileDialog
    ├── FolderDialog
    └── ProgressDialog
```

### Toolbar Controls

```
ToolbarControl [V]
├── CommandControl (V)
├── SeparatorControl (V)
├── SplitButtonControl (V)
└── DropDownControl (V)
```

### Control Definitions

```
ControlDefinition [U]
├── ButtonControlDefinition (U)
├── CheckBoxControlDefinition (U)
└── ListControlDefinition (U)
    └── ListItems
        └── ListItem
```

### Command System

```
CommandDefinition
└── Command
    ├── CommandInputs
    │   └── CommandInput [W]
    ├── CommandCreatedEvent
    ├── CommandEvent
    ├── ValidateInputsEvent
    ├── InputChangedEvent
    ├── KeyboardEvent
    └── MouseEvent
```

### Command Inputs

```
CommandInput [W]
├── BoolValueCommandInput (W)
├── ValueCommandInput (W)
├── SelectionCommandInput (W)
├── StringValueCommandInput (W)
├── DropDownCommandInput (W)
├── MultiSelectCommandInput (W)
├── ButtonRowCommandInput (W)
├── FloatSliderCommandInput (Z)
├── IntegerSliderCommandInput (Z)
├── SliderCommandInput (W) [Z]
├── TextBoxCommandInput (W)
├── FloatSpinnerCommandInput (W)
├── IntegerSpinnerCommandInput (W)
├── GroupCommandInput (W)
├── ImageCommandInput (W)
├── RadioButtonCommandInput (W)
├── TabCommandInput (W)
├── TableCommandInput (W)
├── AngleValueCommandInput (W)
├── DistanceValueCommandInput (W)
└── DirectionCommandInput (W)
```

### Events

```
ApplicationEvent
ApplicationCommandEvent
CommandCreatedEvent
CommandEvent
DocumentEvent
SelectionEvent
WebRequestEvent
WorkspaceEvent
MarkingMenuEvent
CustomEvent
```

### Marking Menus

```
MarkingMenuEventArgs
├── LinearMarkingMenu
└── RadialMarkingMenu
```

---

## Import/Export

### Export Manager

```
ExportManager
└── ExportOptions [AA]
    ├── FusionArchiveExportOptions (AA)
    ├── IGESExportOptions (AA)
    ├── SATExportOptions (AA)
    ├── SMTExportOptions (AA)
    ├── STEPExportOptions (AA)
    └── STLExportOptions (AA)
```

### Import Manager

```
ImportManager
└── ImportOptions [CC]
    ├── FusionArchiveImportOptions (CC)
    ├── IGESImportOptions (CC)
    ├── SATImportOptions (CC)
    ├── SMTImportOptions (CC)
    ├── STEPImportOptions (CC)
    └── DXF2DImportOptions
```

---

## CAM (Computer-Aided Manufacturing)

```
CAM (A)
├── Setups
│   └── Setup
├── Operations
│   └── Operation
│       └── ChildOperationList
├── CAMFolders
│   └── CAMFolder
├── CAMPatterns
│   └── CAMPattern
├── GenerateToolpathFuture
└── MachiningTime
```

---

## Custom Graphics

### Custom Graphics Structure

```
Component
└── CustomGraphicsGroups
    └── CustomGraphicsGroup (GG)
        └── CustomGraphicsEntity [GG]
            ├── CustomGraphicsCurve (GG)
            ├── CustomGraphicsLines (GG)
            ├── CustomGraphicsMesh (GG)
            ├── CustomGraphicsPointSet (GG)
            ├── CustomGraphicsBRepBody (GG)
            └── CustomGraphicsGroup (GG)
```

### Color Effects

```
CustomGraphicsColorEffect [HH]
├── CustomGraphicsSolidColorEffect (HH)
├── CustomGraphicsVertexColorEffect (HH)
├── CustomGraphicsAppearanceColorEffect (HH)
└── CustomGraphicsBasicMaterialColorEffect (HH)
```

### View Settings

```
CustomGraphicsBillBoard
CustomGraphicsViewPlacement
CustomGraphicsViewScale
```

---

## 3D Geometry

### 3D Curves

```
Curve3D [H]
├── Arc3D (H)
├── Circle3D (H)
├── Ellipse3D (H)
├── EllipticalArc3D (H)
├── Line3D (H)
├── InfiniteLine3D (H)
└── NurbsCurve3D (H)
```

### Surfaces

```
Surface [J]
├── Plane (J)
├── Sphere (J)
├── Torus (J)
├── Cylinder (J)
├── Cone (J)
├── EllipticalCone (J)
├── EllipticalCylinder (J)
└── NurbsSurface (J)
```

### Evaluators

```
CurveEvaluator3D
SurfaceEvaluator
```

---

## 2D Geometry

### 2D Curves

```
Curve2D [G]
├── Arc2D (G)
├── Circle2D (G)
├── Ellipse2D (G)
├── EllipticalArc2D (G)
├── Line2D (G)
└── NurbsCurve2D (G)
```

### Evaluator

```
CurveEvaluator2D
```

---

## 3D Math

```
Point3D
Vector3D
Matrix3D
BoundingBox3D
```

---

## 2D Math

```
Point2D
Vector2D
Matrix2D
BoundingBox2D
```

---

## Miscellaneous

### Collections and Utilities

```
ObjectCollection
Attributes
└── Attribute
Color
ValueInput
Entity
Path
└── PathEntity
SketchEntityList
```

### Physical Properties

```
PhysicalProperties
AreaProperties
```

### Document References

```
DocumentReferences
└── DocumentReference
```

### Units Manager

```
FusionUnitsManager
```

### User

```
User
```

### Viewport and Camera

```
ViewPort
└── Camera
```

### Product Usage

```
ProductUsageData
```
