import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
model_path = "inception-mbzuai/jais-13b-chat"
device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto",local_files_only=False, offload_folder="./jais_chat_offloaded_folder", trust_remote_code=True)


def get_response(text,tokenizer=tokenizer,model=model):
    print(f"The used device :{device}")
    input_ids = tokenizer(text, return_tensors="pt").input_ids
    inputs = input_ids.to(device)
    input_len = inputs.shape[-1]
    generate_ids = model.generate(
        inputs,
        top_p=0.9,
        temperature=0.3,
        max_length=2048-input_len,
        min_length=input_len + 4,
        repetition_penalty=1.2,
        do_sample=True,
    )
    response = tokenizer.batch_decode(
        generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True
    )[0]
    response = response.split("### Response: [|AI|]")
    return response


ar_ques= "ما هي الحلول الاقتصادية لازمة سعر صرف الدولار في مصر وكذلك مشكلة التخضم ؟"
arabic_ans = get_response(ar_ques)
print (arabic_ans)

# en_ques = "What is the suggested actions from medical perspective i can make from a nation prospective if there is a train accident with casualties and injuries. ?"
# english_ans = get_response(en_ques)
# print (english_ans)