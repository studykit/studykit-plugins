---
name: Fusion 360 API Guide
disable-model-invocation: true
description: This skill should be used when the user asks about "Fusion 360 API", "Fusion API", "Fusion add-in", "Fusion script", "Fusion Python", "adsk.core", "adsk.fusion", "adsk.cam", "Fusion object model", "Fusion custom feature", "Fusion command", "Fusion UI customization", "Fusion CAM API", "Fusion event handling", "Fusion sketch", "Fusion extrude", or needs guidance on Autodesk Fusion 360 API development, scripting, add-in creation, or automation.
---

# Fusion 360 API Development Guide

This skill provides comprehensive documentation for developing scripts and add-ins using the Autodesk Fusion 360 API. The API enables automation of design tasks, creation of custom features, UI customization, and CAM programming.

## Overview

The Fusion 360 API primarily supports **Python** for scripts and add-ins development.

## Reference Documentation

All reference materials are located in the following folders within this skill directory:

| Folder | Contents |
|--------|----------|
| `references/user-manual/` | Conceptual guides and tutorials |
| `references/api-reference/` | Class, method, property, and enum documentation |
| `references/samples/` | Code sample documentation |
| `references/images/` | Diagrams and screenshots |
| `sample-codes/` | Complete working add-in examples |
| `libs/adsk/` | Python type stubs for IDE support |

## Core Concepts

### Object Model

Fusion 360 uses a hierarchical object model:

```
Application
  └── Documents (collection)
       └── Document
            └── Products
                 ├── Design (modeling)
                 │    └── rootComponent
                 │         ├── Sketches
                 │         ├── Features
                 │         ├── Bodies
                 │         └── Occurrences
                 └── CAM (manufacturing)
```

See `references/user-manual/Fusion_API_Object_Model.md` for the complete class hierarchy including all Feature types, Sketch entities, Joint types, Command inputs, and their relationships. Use this file when looking up specific class names or understanding parent-child relationships between API objects. For conceptual explanation, see `references/user-manual/BasicConcepts_UM.md`.

### Python API Modules

The Fusion 360 Python API consists of these core modules:

| Module | Purpose | Documentation |
|--------|---------|---------------|
| `adsk.core` | Application, UI, geometry, events | Core functionality |
| `adsk.fusion` | Design features, sketches, bodies | Modeling operations |
| `adsk.cam` | CAM operations, toolpaths | Manufacturing |
| `adsk.drawing` | Drawing views, annotations | 2D documentation |

Python type definitions for API classes, methods, and enums are in `libs/adsk/`.

### Script vs Add-In

| Feature | Script | Add-In |
|---------|--------|--------|
| Lifetime | Runs once, then stops | Runs until stopped |
| UI Integration | Cannot add UI elements | Can add commands, panels |
| Use Case | One-time automation | Persistent features |

See `references/user-manual/WritingDebugging_UM.md` for creation guide.

## Common Development Patterns

### Getting Application Reference

```python
import adsk.core, adsk.fusion

app = adsk.core.Application.get()
ui = app.userInterface
design = adsk.fusion.Design.cast(app.activeProduct)
rootComp = design.rootComponent
```

### Creating Features

```python
# Get or create a sketch
sketches = rootComp.sketches
xyPlane = rootComp.xYConstructionPlane
sketch = sketches.add(xyPlane)

# Draw geometry
circles = sketch.sketchCurves.sketchCircles
circle = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), 2)

# Create extrusion
profile = sketch.profiles.item(0)
extrudes = rootComp.features.extrudeFeatures
extInput = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
distance = adsk.core.ValueInput.createByReal(5)  # 5 cm (internal units)
extInput.setDistanceExtent(False, distance)
extrude = extrudes.add(extInput)
```

### Event Handling

```python
class MyCommandCreatedHandler(adsk.core.CommandCreatedEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        eventArgs = adsk.core.CommandCreatedEventArgs.cast(args)
        cmd = eventArgs.command
        # Set up command inputs and handlers

# Register handler
cmdDef = ui.commandDefinitions.addButtonDefinition('myCommand', 'My Command', 'Description')
onCommandCreated = MyCommandCreatedHandler()
cmdDef.commandCreated.add(onCommandCreated)
handlers.append(onCommandCreated)  # Keep reference to prevent garbage collection
```

### Units

Fusion 360 API uses internal database units:
- **Length**: Centimeters (cm)
- **Angle**: Radians

Use `UnitsManager` for conversion:

```python
um = design.unitsManager
# Convert user expression to internal value
internalVal = um.evaluateExpression('25 mm', 'cm')
# Format internal value for display
displayStr = um.formatInternalValue(5.0, 'cm', True)  # "50 mm"
```

See `references/user-manual/Units_UM.md` for details.

## Key Documentation Files

### Getting Started

| File | Topic |
|------|-------|
| `references/user-manual/WelcomeToSDK_UM.md` | API introduction |
| `references/user-manual/BasicConcepts_UM.md` | Object model, collections, inputs |
| `references/user-manual/WritingDebugging_UM.md` | Creating scripts and add-ins |
| `references/user-manual/PythonSpecific_UM.md` | Python-specific guidance |

### UI and Commands

| File | Topic |
|------|-------|
| `references/user-manual/UserInterface_UM.md` | UI customization overview |
| `references/user-manual/Commands_UM.md` | Creating commands |
| `references/user-manual/CommandInputs_UM.md` | Command input types |
| `references/user-manual/Events_UM.md` | Event handling |
| `references/user-manual/Palettes_UM.md` | HTML palettes |

### Modeling

| File | Topic |
|------|-------|
| `references/user-manual/BRepGeometry_UM.md` | B-Rep topology |
| `references/user-manual/ComponentsProxies_UM.md` | Document/assembly structure |
| `references/user-manual/CustomFeatures_UM.md` | Creating custom features |
| `references/user-manual/CustomGraphics_UM.md` | Drawing custom graphics |

### CAM (Manufacturing)

| File | Topic |
|------|-------|
| `references/user-manual/CAMIntroduction_UM.md` | CAM API overview |
| `references/user-manual/CAMParameters_UM.md` | Operation parameters |
| `references/user-manual/CAMLibraries_UM.md` | Tool and template libraries |
| `references/user-manual/VolumetricModeling_UM.md` | Stock and fixtures |

## Working Add-In Examples

Complete add-in examples are in `sample-codes/`:

| Example | Description |
|---------|-------------|
| `CustomPocket/` | Custom feature with parameters and UI |
| `RoundEmbossExample/` | Custom emboss feature |
| `UICustomizationSamplePython/` | Toolbar and command customization |

Each add-in includes:
- Main Python script (`.py`)
- Manifest file (`.manifest`)
- Resources folder with icons

## API Reference Lookup

API reference files are in `references/api-reference/` with naming convention:
- `ClassName.md` - Class overview
- `ClassName_propertyName.md` - Property documentation
- `ClassName_methodName.md` - Method documentation

Example: To find `ExtrudeFeatures.add()` method:
```
references/api-reference/ExtrudeFeatures_add.md
```

## Best Practices

1. **Keep Handler References**: Store event handlers in a global list to prevent garbage collection
2. **Use Transactions**: Wrap operations for undo support
3. **Handle Errors**: Use try/except and provide user feedback
4. **Clean Up on Stop**: Remove UI elements when add-in stops
5. **Use Base Features**: For non-parametric operations, use `BaseFeature` within parametric timeline
6. **Internal Units**: Always use cm and radians in API calls, convert for display
