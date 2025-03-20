import Form from "./components/Form";
import FormState from "./components/FormState";
import HookForm from "./components/HookForm";

function App() {
  return (
    <>
      <div className="w-7xl mx-auto px-4 py-8">
        <Form />
        <h2>Form 2</h2>
        <FormState />
        <h2>Form 3</h2>
        <HookForm />
      </div>
    </>
  );
}

export default App;
